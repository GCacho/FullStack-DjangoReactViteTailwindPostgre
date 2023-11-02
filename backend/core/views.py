# from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Customer
from books.models import Book, BookTitle

def home_view(request):
    value = "Hello World! :)"
    qs = Customer.objects.all()
    # obj = Book.objects.get(id=1)
    obj = BookTitle.objects.get(id=1) # get all objects on books (check model on the book class)
    books = obj.books.all() # To check books with the same title
    print(books)

    context = {
        'hello_key':value,
        'qs':qs,
        'obj':obj,
    }

    return render(request,'main.html', context)