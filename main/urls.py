from django.contrib import admin
from django.urls import path, include
from accounts.views import *
from book.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<int:page_order>/', BookList.as_view()),
    path('', BookList.as_view()),
    path('book-detail/<int:book_order>/', BookDetail.as_view(), name='book-detail'),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/book/', include('book.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
