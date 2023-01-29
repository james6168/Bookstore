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


class BookImageIdSerializer(Serializer):
    id = serializers.IntegerField()


class BookSerializer(ModelSerializer):

    images = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ("name", "description", "price", "images", "id", "user")
        extra_kwargs = {
            "name": {"required": True}
        }


class AdditionalBookSerializer(ModelSerializer):
    images = BookImageIdSerializer(many=True)

    class Meta:
        model = Book
        fields = ("name", "description", "price", "images", "id", "user")
        extra_kwargs = {
            "name": {"required": True}
        }

    def create(self, validated_data):
        book_image_id_list = [ordered_dict.get("id") for ordered_dict in validated_data.pop("images")]
        print(book_image_id_list)
        images = BookImage.objects.filter(id__in=book_image_id_list)
        instance = Book.objects.create(**validated_data)
        instance.images.set(images)
        return instance


class BookIdSerializer(Serializer):
    id = serializers.IntegerField()


class OrderSerializer(ModelSerializer):
    books = BookIdSerializer(many=True)

    class Meta:
        model = Order
        fields = ("extra_info", "delivery_type", "books", "user")

    def create(self, validated_data):
        book_id_list = [ordered_dict.get("id") for ordered_dict in validated_data.pop("books")]
        books = Book.objects.filter(id__in=book_id_list)
        total_sum = 0
        for each_book in books:
            total_sum += getattr(each_book, "price")
        validated_data.update({"total_sum": total_sum})
        instance = Order.objects.create(**validated_data)
        instance.books.set(books)
        return instance












