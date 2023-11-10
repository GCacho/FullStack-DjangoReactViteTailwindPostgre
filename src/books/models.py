import uuid
from django.db import models
from publishers.models import Publisher
from authors.models import Author
from django.utils.text import slugify
from django.urls import reverse
from rentals.rental_choices import STATUS_CHOICES
# Imports for QrCode Generation -> Documentation https://pypi.org/project/qrcode/
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image


# Create your models here.
class BookTitle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True) # Harry Potter -> Harry-Potter w/slug
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Defining methods in models with decorators
    @property
    def books(self):
        return self.my_books.all() # comes from class Book on the title
    
    # Create the absolute url for correct navigation
    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return f"Book Position: {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class Book(models.Model):
    title = models.ForeignKey(BookTitle, on_delete=models.CASCADE, related_name="my_books") # Reverse Relationship: related_name so we can use it on core/views.py ( books = obj.books.all() )
    isbn = models.CharField(max_length=24, blank=True)

    # qr_code
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    # Exporting Book Data
    @property
    def status(self):
        if len(self.rental_set.all()) > 0:
            statuses = dict(STATUS_CHOICES)
            return statuses[self.rental_set.first().status]
        return False
    
    
    # Create de Book ID
    def save(self, *args, **kwargs):
        if not self.isbn:
            self.isbn = str(uuid.uuid4()).replace('-','')[:24].lower()

            # Generate qr code if the book id exists
            qrcode_img = qrcode.make(self.isbn)
            canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
            canvas.paste(qrcode_img)
            fname = f'qr_code-{self.isbn}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            self.qr_code.save(fname, File(buffer), save=False)
            canvas.close()

        super().save(*args, **kwargs)