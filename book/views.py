from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.response import Response
from book.permissions import *
from book.serializers import *
from book.models import Book
from django.views.generic import TemplateView
from book.paginations import BookListPagination
from rest_framework.permissions import *
from rest_framework import status


class BookListAPIView(ListAPIView):
    permission_classes = [IsAuthorOrReadOnly,]
    pagination_class = BookListPagination
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailAPIView(GenericAPIView):
    permission_classes = [IsAuthorOrReadOnly, ]
    serializer_class = BookSerializer

    def get(self, request):
        book_id = request.GET.get("id")
        serializer = BookSerializer(Book.objects.get(id=book_id))
        return Response(serializer.data)


class BookImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsBookOwnerOnly]
    serializer_class = BookImageSerializer
    queryset = BookImage.objects.all()


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsBookOwnerOnly]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookImageCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookImageSerializer
    queryset = BookImage.objects.all()

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BookCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def create(self, request, *args, **kwargs):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data["user"] = request.user.id
        request.data._mutable = _mutable
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BookList(TemplateView):
    template_name = "book_store.html"


class BookDetail(TemplateView):
    template_name = "book_detail.html"

