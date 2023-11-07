from django.core.management.base import BaseCommand
from authors.models import Author
from publishers.models import Publisher
from books.models import BookTitle, Book
from customers.models import Customer
from django_countries.fields import Country 
import random

class Command(BaseCommand):

    help = "Generaty dummy data for testing purposes"

    def handle(self, *args, **kwargs):
        # Generate Authors
        authors_list = ['Guillermo Cacho', 'Paola Perez', 'Santiago Cacho', 'David Kakero', 'Chavo Delocho']
        for name in authors_list:
            Author.objects.create(name=name)

        # Generate Publishers
        publisher_list = [
            {'name':'X books', 'country':Country(code='us')},
            {'name':'Y books', 'country':Country(code='es')},
            {'name':'Z books', 'country':Country(code='mx')},
            {'name':'Next', 'country':Country(code='pl')},
        ]

        for item in publisher_list:
            Publisher.objects.create(**item)

        # Generate Book Titles
        book_titles_list = ['Star Wurs', 'Lord of the wings', 'Witcher', 'Trololol']
        publishers = [x.name for x in Publisher.objects.all()]
        items = zip(book_titles_list, publishers)

        for item in items:
            author = Author.objects.order_by('?')[0]
            publisher = Publisher.objects.get(name=item[1])
            BookTitle.objects.create(title=item[0], publisher=publisher, author=author)

        # Generate Books
        book_titles = BookTitle.objects.all()
        for title in book_titles:
            quantity = random.randint(1,5)
            for i in range(quantity):
                Book.objects.create(title=title)

        # Generate Customers
        customers_list = [
            {'first_name':'Juan', 'last_name':'Perezoso'},
            {'first_name':'Marco', 'last_name':'Polo'},
            {'first_name':'Benito', 'last_name':'Islas'},
        ]
        for item in customers_list:
            Customer.objects.create(**item)