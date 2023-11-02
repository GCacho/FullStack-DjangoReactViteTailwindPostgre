from django.urls import path
from .views import book_title_list_view, book_title_detail_view

app_name = 'books'


urlpatterns = [
    # Comes from books/views.py | http://127.0.0.1:8000/books/1/ example
    path('', book_title_list_view, name='main'),
    path('<pk>/', book_title_detail_view, name='detail'), # <pk> - primary key, <str:text> - string, <slug> - slug
]
