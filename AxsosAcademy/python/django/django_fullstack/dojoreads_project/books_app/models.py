from django.db import models
from login_app.models import User

class Author(models.Model):
    name       = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title      = models.CharField(max_length=255)
    author     = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    review     = models.TextField()
    rating     = models.IntegerField()
    user       = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE
    )
    book       = models.ForeignKey(
        Book, related_name="reviews", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)