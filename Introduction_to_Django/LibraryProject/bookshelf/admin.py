from django.contrib import admin

# Register your models here.from django.contrib import admin
from .models import Book

# Registering the Book model
admin.site.register(Book)

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Filters for publication year and author
    list_filter = ('publication_year', 'author')

    # Search functionality for title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin configuration
admin.site.register(Book, BookAdmin)
