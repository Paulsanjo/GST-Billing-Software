from django.contrib import admin

# from import_export import resources
from .models import Book

admin.site.register(Book)

# class BookResource(resources.ModelResource):

#     class Meta:
#         model = Book