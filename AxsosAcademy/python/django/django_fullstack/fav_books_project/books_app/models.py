from django.db import models
from login_app.models import User

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title'].strip()) == 0:
            errors['title'] = "Title is required."
        if len(postData['desc'].strip()) < 5:
            errors['desc'] = "Description must be at least 5 characters."
        return errors

class Book(models.Model):
    title          = models.CharField(max_length=255)
    desc           = models.TextField()
    uploaded_by    = models.ForeignKey(
        User, related_name="books_uploaded", on_delete=models.CASCADE
    )
    users_who_like = models.ManyToManyField(
        User, related_name="liked_books"
    )
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    objects        = BookManager()