from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    books = models.ManyToManyField(Book, related_name='authors')
   
