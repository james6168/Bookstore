from django.shortcuts import render
from rest_framework.generics import ListAPIView
from book.permissions import IsAuthorOrReadOnly
from book.serializers import BookSerializer
from book.models import Book
from django.views.generic import TemplateView


class BookListAPIView(ListAPIView):

    permission_classes = [IsAuthorOrReadOnly,]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookList(TemplateView):
    template_name = "book_store.html"

