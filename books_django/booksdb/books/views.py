
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from books.models import book
from bookdb import BookDB
from django.template import Context,loader

def index(books):
    book_list = book.objects.all().orderby('author')
    return render_to_response('books/index.html', { 'book_list' : book_list }

def info(request,find_book_id):
    b = get_object_or_404(Book, pk=id)
    return render_to_response('books/detail.html', {'book': b})

def my_admin(request):
    book_count=book.objects.all().count()
    t = loader.get_template('my_admin.html')
    c = Context({
        'book_count': book_count,
    })
    return HttpResponse(t.render(c))

def my_admin_purge(request):
    book.objects.all().delete()
    book_count=book.objects.all().count()
    t = loader.get_template('my_admin.html')
    c = Context({
        'book_count': book_count,
    })
    return HttpResponse(t.render(c))

def my_admin_load_BooksDB(request):
    my_books=BookDB()

    book_count=-1
    for my_book in my_books.titles():

        db_book=book()
        
        db_book.book_id=my_book['id']
        db_book.isbn=my_books.title_info(my_book['id'])['isbn'].replace('-','')
        
        db_book.title= my_books.title_info(my_book['id'])['title']
        db_book.author= my_books.title_info(my_book['id'])['author']
        db_book.publisher= my_books.title_info(my_book['id'])['publisher']
        print db_book.book_id,db_book.isbn        
        db_book.save()
        db_book=None
        book_count=book.objects.all().count()
        t = loader.get_template('my_admin.html')
        c = Context({
                'book_count': book_count,
            })
    return HttpResponse(t.render(c))
