from django.shortcuts import render
from .models import BookTitle
from django.views.generic import ListView
# Create your views here.

class BookTitleListView(ListView):
    # model = BookTitle
    # queryset = BookTitle.objects.all()[:3] # Just send the first 3 objects
    # queryset = BookTitle.objects.all().order_by('-created') # Reverse order
    template_name = 'books/main.html'
    context_object_name = 'qs'

    def get_queryset(self):
        parameter = 'S'
        return BookTitle.objects.filter(title__startswith=parameter)
    

# -------------------------------------------------------------------------------------------------

# def book_title_list_view(request): # Same as -> class BookTitleListView(ListView): on the top of this file.
#     qs = BookTitle.objects.all()
#     return render(request,'books/main.html', {'qs':qs})


def book_title_detail_view(request, pk):
    obj = BookTitle.objects.get(pk=pk)
    return render(request, 'books/detail.html', {'obj':obj})