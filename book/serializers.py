from rest_framework.serializers import ModelSerializer
from book.models import *


class BookImageSerializer(ModelSerializer):
    class Meta:
        model = BookImage
        fields = "__all__"


class BookSerializer(ModelSerializer):

    images = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ("name", "description", "price", "created_at", "updated_at", "images")





