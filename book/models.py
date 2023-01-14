from django.db import models


class BookImage(models.Model):
    book_image = models.ImageField(upload_to='book')
    file_name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.file_name


class AuthorImage(models.Model):
    author_image = models.ImageField(upload_to='authors')
    file_name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.file_name


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='No description')
    price = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ManyToManyField(BookImage, related_name='book_images', blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name='books', blank=True)
    images = models.ManyToManyField(AuthorImage, related_name='author_images', blank=True)

    def __str__(self):
        return self.name




