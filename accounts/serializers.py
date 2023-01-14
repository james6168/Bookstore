from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class RegisterSerializer(ModelSerializer):
    password1 = CharField(min_length=8, write_only=True)
    password2 = CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def validate_email(self, data):
        user = User.objects.filter(email=data).exists
        if not user:
            raise ValidationError(f"Such user with that {data} exists")
        return data

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        if password1 != password2:
            raise ValidationError(f"Passwords are not equal each other")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password1")
        del validated_data["password2"]
        user = User.objects.create_user(**validated_data, password=password)
        user.is_active = True
        user.save()
        return user


class LoginSerializer(TokenObtainPairSerializer):
    email = CharField(max_length=30, write_only=True)
    password = CharField(max_length=100, write_only=True)

    def validate(self, attrs):
        user = authenticate(email=attrs.pop("email"), password=attrs.pop("password"))

        if not user:
            raise ValidationError({"error": "Such user does not exist, or invalid credentials were provided"})

        if user and user.is_active:
            refresh = self.get_token(user)
            attrs["refresh"] = str(refresh)
            attrs["access"] = str(refresh.access_token)

        return attrs






