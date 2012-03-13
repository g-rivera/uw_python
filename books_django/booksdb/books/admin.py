from books.models import Book
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    attribs = ['title', 'author', 'isbn', 'publisher', 'pub_date']
    list_attribs = ('title', 'author', 'pub_date')
    
admin.site.register(Book, BookAdmin)
