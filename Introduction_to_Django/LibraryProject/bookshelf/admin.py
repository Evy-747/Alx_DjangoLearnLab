from django.contrib import admin

# Register your models here.from django.contrib import admin
from .models import Book

# Registering the Book model
admin.site.register(Book)

