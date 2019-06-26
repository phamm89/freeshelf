from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.utils import timezone
from django.contrib.auth.models import User

# Created Models
class Category(models.Model):
    """Model representing a book category."""
    book_category = models.CharField(max_length=200, help_text='Enter a book category (e.g. CSS, HTML, Javascript, Python, R)')
    
    class Meta:
        """Plural name for category to override category+s"""
        verbose_name_plural = "categories"

    def __str__(self):
        """String for representing the Model object."""
        return self.book_category
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for a book category."""
        return reverse('category-detail', args=[str(self.id)])


class Book(models.Model):
    """Model representing a book added to Freeshelf."""
    book_title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    book_author = models.ForeignKey('BookAuthor', on_delete=models.SET_NULL, null=True)
    
    book_url = models.URLField(max_length=200, unique=True, help_text='Enter the unique URL of the book.')
    book_description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    db_date_added = models.DateTimeField(auto_now_add=True)
    
    # ManyToManyField used because category can contain many books. Books can belong to multiple categories.
    book_category = models.ManyToManyField(Category, help_text='Select categories for this book')
    
    class Meta:
        ordering = ['-db_date_added']

    def __str__(self):
        """String for representing the Model object."""
        return self.book_title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


class BookAuthor(models.Model):
    """Model representing an author."""
    book_author = models.CharField(max_length=200, help_text='Enter the name of the author')

    def __str__(self):
        """String for representing the Model object."""
        return self.book_author