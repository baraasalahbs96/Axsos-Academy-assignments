from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least 2 characters."
        if len(postData['alias']) < 2:
            errors['alias'] = "Alias must be at least 2 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format."
        if User.objects.filter(email=postData['email']).exists():
            errors['email_taken'] = "Email already registered."
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters."
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
    name       = models.CharField(max_length=255)
    alias      = models.CharField(max_length=255)
    email      = models.CharField(max_length=255)
    password   = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects    = UserManager()