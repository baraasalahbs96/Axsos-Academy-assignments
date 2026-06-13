from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    email      = models.CharField(max_length=45)
    password   = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title         = models.CharField(max_length=255)
    desc          = models.TextField()
    # One-to-Many: user uploads many books
    uploaded_by   = models.ForeignKey(
        User,
        related_name="books_uploaded",
        on_delete=models.CASCADE
    )
    # Many-to-Many: users who liked this book
    users_who_like = models.ManyToManyField(
        User,
        related_name="liked_books"
    )
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title