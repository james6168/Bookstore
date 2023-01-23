from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.response import Response
from book.permissions import *
from book.serializers import BookSerializer
from book.models import Book
from django.views.generic import TemplateView
from book.paginations import BookListPagination


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


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsBookOwnerOnly]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookList(TemplateView):
    template_name = "book_store.html"


class BookDetail(TemplateView):
    template_name = "book_detail.html"

