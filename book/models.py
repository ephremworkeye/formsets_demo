from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('book:author_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')
    