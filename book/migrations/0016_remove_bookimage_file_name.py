# Generated by Django 4.1.5 on 2023-01-26 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookimage',
            name='file_name',
        ),
    ]
