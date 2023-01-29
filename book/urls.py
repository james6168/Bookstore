from django.urls import path
from book.views import *

urlpatterns = [
    path('book-list/', BookListAPIView.as_view()),
    path('', BookDetailAPIView.as_view()),
    path('book-update/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('book-create/', BookCreateAPIView.as_view()),
    path('book-image-create/', BookImageCreateAPIView.as_view()),
    path('book-image-update/<int:pk>/', BookImageRetrieveUpdateDestroyAPIView.as_view()),
    path('order-create/', OrderCreateApiView.as_view()),
    path('order-list/', OrderListAPIView.as_view())
]