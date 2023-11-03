from django.shortcuts import render
from .models import BookTitle
from django.views.generic import ListView, FormView
from .forms import BookTitleForm
from django.urls import reverse, reverse_lazy
# Create your views here.

class BookTitleListView(FormView, ListView):
    # model = BookTitle
    # queryset = BookTitle.objects.all()[:3] # Just send the first 3 objects
    # queryset = BookTitle.objects.all().order_by('-created') # Reverse order
    template_name = 'books/main.html'
    context_object_name = 'qs'
    form_class = BookTitleForm

    def get_queryset(self): # A QuerySet
        parameter = 'L'
        return BookTitle.objects.filter(title__startswith=parameter)
    
    def get_success_url(self): # To send the form to the DB with the correct URL
        return self.request.path
    
    def form_valid(self, form): # To save the form data into the DB
        form.save()
        return super().form_valid(form)
    

# -------------------------------------------------------------------------------------------------

# def book_title_list_view(request): # Same as -> class BookTitleListView(ListView): on the top of this file.
#     qs = BookTitle.objects.all()
#     return render(request,'books/main.html', {'qs':qs})


def book_title_detail_view(request, pk):
    obj = BookTitle.objects.get(pk=pk)
    return render(request, 'books/detail.html', {'obj':obj})