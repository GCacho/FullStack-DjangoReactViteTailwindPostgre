from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import BookTitle, Book
from django.views.generic import ListView, FormView
from .forms import BookTitleForm
from django.contrib import messages
from django.http import JsonResponse
import string
# Create your views here.

class BookTitleListView(FormView, ListView):
    model = BookTitle
    template_name = 'books/main.html'
    context_object_name = 'qs'
    form_class = BookTitleForm
    i_instance = None
    paginate_by = 36

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

class BookListView(ListView):
    template_name = 'books/detail.html'
    paginate_by = 2


    def get_queryset(self):
        title_slug = self.kwargs.get('slug')
        return Book.objects.filter(title__slug = title_slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title_slug = self.kwargs.get('slug')
        if title_slug:
            book_title = Book.objects.filter(title__slug=title_slug).first()
            if book_title:
                context['book_title'] = book_title.title
        return context


def book_first_letter_view(request, letter):
    books = BookTitle.objects.filter(title__istartswith=letter)
    return render(request, 'books/first_letter.html', {'books': books, 'letter': letter})

def search_books(request):
    query = request.GET.get('q', '')
    books = BookTitle.objects.filter(title__icontains=query).values('title', 'slug')[:10]  # Limitando los resultados a 10
    return JsonResponse(list(books), safe=False)