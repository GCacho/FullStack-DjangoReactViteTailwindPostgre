from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import BookTitle, Book
from django.views.generic import ListView, FormView
from .forms import BookTitleForm
from django.contrib import messages
import string
# Create your views here.

class BookTitleListView(FormView, ListView):
    model = BookTitle
    template_name = 'books/main.html'
    context_object_name = 'qs'
    form_class = BookTitleForm
    i_instance = None

    def get_success_url(self): # To send the form to the DB with the correct URL
        return self.request.path
    
    def get_queryset(self):
        parameter = self.kwargs.get('letter')  # Asegurándose de que esté en minúsculas
        if parameter:
            books = BookTitle.objects.filter(title__istartswith=parameter)
        else:
            books = BookTitle.objects.all()
        return books.order_by('title')
    
    def form_valid(self, form): # To save the form data into the DB
        self.i_instance = form.save()
        messages.add_message(self.request, messages.INFO, f"Book Title: ({self.i_instance.title}) has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        self.object_list = self.get_queryset()
        messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        letters = list(string.ascii_lowercase)
        context['letters'] = letters
        context['selected_letter'] = self.kwargs.get('letter')
        return context
    

# -------------------------------------------------------------------------------------------------

# def book_title_list_view(request): # Same as -> class BookTitleListView(ListView): on the top of this file.
#     qs = BookTitle.objects.all()
#     return render(request,'books/main.html', {'qs':qs})


# def book_title_detail_view(request, **kwargs):
#     slug = kwargs.get('slug')
#     obj = BookTitle.objects.get(slug=slug)
#     return render(request, 'books/detail.html', {'obj':obj})


class BookListView(ListView):
    template_name = 'books/detail.html'


    def get_queryset(self):
        title_slug = self.kwargs.get('slug')
        return Book.objects.filter(title__slug = title_slug)



def book_first_letter_view(request, letter):
    books = BookTitle.objects.filter(title__istartswith=letter)
    return render(request, 'books/first_letter.html', {'books': books, 'letter': letter})