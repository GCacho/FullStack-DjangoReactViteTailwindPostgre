from django.urls import path
from .views import BookTitleListView, BookListView, search_books

app_name = 'books'


urlpatterns = [
    # Comes from books/views.py | http://127.0.0.1:8000/books/1/ example
    path('', BookTitleListView.as_view(), {'letter':None}, name='main'),
    path('search/', search_books, name='search_books'),
    path('<str:letter>/', BookTitleListView.as_view(), name='main'),
    path('<str:letter>/<slug>/', BookListView.as_view(), name='detail'), # <pk> - primary key, <str:text> - string, <slug> - slug
    
]
