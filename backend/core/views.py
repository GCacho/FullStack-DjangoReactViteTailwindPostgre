# from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Customer
from books.models import Book

def home_view(request):
    value = "Hello World! :)"
    qs = Customer.objects.all()
    obj = Book.objects.get(id=1)
    context = {
        'hello_key':value,
        'qs':qs,
        'book':obj,
    }

    return render(request,'main.html', context)