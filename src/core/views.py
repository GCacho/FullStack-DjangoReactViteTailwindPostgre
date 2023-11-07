# from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Customer
from books.models import BookTitle
from django.http import HttpResponseRedirect

# Tailwind Dark Mode
def change_theme(request):
    if 'is_dark_mode' in request.session:
        request.session['is_dark_mode'] = not request.session['is_dark_mode']
    else:
        request.session['is_dark_mode'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Content block to main html
def home_view(request):
    qs = Customer.objects.all()
    # obj = Book.objects.get(id=1)
    obj = BookTitle.objects.get(id=7) # get all objects on books (check model on the book class)
    books = obj.books # To check books with the same title
    print(books)

    context = {
        'qs':qs,
        'obj':obj,
    }

    return render(request,'main.html', context)