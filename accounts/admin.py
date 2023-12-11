from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock', 'genre', 'description', 'isbn') # Add the fields you want to display

admin.site.register(models.User)
admin.site.register(models.Book, BookAdmin) # Register the BookAdmin class for the Book model
