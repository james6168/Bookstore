from django.contrib import admin
from book.models import *

admin.site.register(Book)
admin.site.register(BookImage)
admin.site.register(AuthorImage)
admin.site.register(Author)

