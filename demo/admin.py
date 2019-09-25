from django.contrib import admin
from .models import Book, BookNumber, Character, Author
# Register your models here.

# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['published']
    search_fields = ['title']
    

@admin.register(BookNumber)
class BookNumberAdmin(admin.ModelAdmin):
    list_display = ['isbn_10', 'isbn_13']
    list_filter = ['isbn_10', 'isbn_13']
    search_fields = ['isbn_10', 'isbn_13']
    

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'book']
    list_filter = ['name', 'book']
    search_fields = ['name', 'book']
   
admin.site.register(Author)
