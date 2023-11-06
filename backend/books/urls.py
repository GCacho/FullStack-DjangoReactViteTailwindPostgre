from django.urls import path
from .views import BookTitleListView, book_title_detail_view, book_first_letter_view

app_name = 'books'


urlpatterns = [
    # Comes from books/views.py | http://127.0.0.1:8000/books/1/ example
    path('', BookTitleListView.as_view(), name='main'),
    path('<pk>/', book_title_detail_view, name='detail'), # <pk> - primary key, <str:text> - string, <slug> - slug
    
    path('books/<str:letter>/', book_first_letter_view, name='book-first-letter'),
]
