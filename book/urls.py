from django.urls import path
from book.views import *

urlpatterns = [
    path('book-list/', BookListAPIView.as_view()),
    path('', BookDetailAPIView.as_view()),
    path('book-update/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view())
]