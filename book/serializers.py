from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from book.models import *


class BookImageSerializer(ModelSerializer):

    class Meta:
        model = BookImage
        fields = ("file_name", "book_image", "id", "user")
        extra_kwargs = {
            "file_name": {"required": True}
        }


class BookSerializer(ModelSerializer):

    images = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ("name", "description", "price", "images", "id", "user")
        extra_kwargs = {
            "name": {"required": True}
        }










