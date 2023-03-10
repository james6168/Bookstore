# Generated by Django 4.1.5 on 2023-01-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_remove_author_books_remove_author_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorimage',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='bookimage',
            name='books',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='books', to='book.book'),
        ),
        migrations.AddField(
            model_name='author',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='author_images', to='book.authorimage'),
        ),
        migrations.AddField(
            model_name='book',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='book_images', to='book.bookimage'),
        ),
    ]
