from django.db import models


class BookImage(models.Model):
    book_image = models.ImageField(upload_to='book')


class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    name = models.CharField(max_length=50)


