from django.contrib import admin
from django.urls import path, include
from accounts.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/book/', include('book.urls')),
]
