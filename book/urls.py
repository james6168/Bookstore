from django.urls import path
from book.views import BookListAPIView

urlpatterns = [
    path('book-list/', BookListAPIView.as_view())
]