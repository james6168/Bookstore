from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from accounts.serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny

User = get_user_model()


class RegisterAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer


class LoginView(TemplateView):
    template_name = "login.html"


class RegisterView(TemplateView):
    template_name = "register.html"





