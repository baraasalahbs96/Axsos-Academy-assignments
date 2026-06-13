from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format."
        if User.objects.filter(email=postData['email']).exists():
            errors['email_taken'] = "Email already registered."
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        if postData['password'] != postData['confirm_pw']:
            errors['confirm'] = "Passwords do not match."
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if not user:
            errors['login'] = "Invalid email or password."
        else:
            if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                errors['login'] = "Invalid email or password."
        return errors

class User(models.Model):
    email       = models.CharField(max_length=255)
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    password    = models.CharField(max_length=255)
    user_level  = models.IntegerField(default=1)  # 1=normal, 9=admin
    description = models.TextField(default="")
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects     = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Message(models.Model):
    content    = models.TextField()
    sender     = models.ForeignKey(
        User, related_name="sent_messages", on_delete=models.CASCADE
    )
    receiver   = models.ForeignKey(
        User, related_name="received_messages", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content    = models.TextField()
    user       = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE
    )
    message    = models.ForeignKey(
        Message, related_name="comments", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)