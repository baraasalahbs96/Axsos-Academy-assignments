from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        if not post_data.get('first_name') or not post_data.get('last_name') or \
            not post_data.get('email') or not post_data.get('password') or \
            not post_data.get('confirm_pw'):
                errors['required'] = 'all fields are required'
        if post_data.get('first_name') and len(post_data.get('first_name')) < 2:
            errors['first_name'] = "first name and last name must be at least 2 characters"
        if post_data.get('last_name') and len(post_data.get('last_name')) < 2:
            errors['last_name'] = "first name and last name must be at least 2 characters"
        if post_data.get('email'):
            if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', post_data.get('email')):
                errors['email'] = "Email must be a valid email"
            elif User.objects.filter(email=post_data.get('email')).exists():
                errors['email_exists'] = "Email already exists"
        if post_data.get('password') and len(post_data.get('password')) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if post_data.get('password') and post_data.get('confirm_pw'):
                if post_data['password'] != post_data['confirm_pw']:
                    errors['match'] = "Passwords do not match"
        return errors
    
    def login_validator(self, post_data):
        errors = {}
        user = User.objects.filter(email=post_data.get('email')).first()
        if not user:
            errors['login'] = "Invalid email or password"
            return errors
        if not bcrypt.checkpw(post_data.get('password').encode(), user.password.encode()):
            errors['login'] = "Invalid email or password"
        return errors
    
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

class TreeManager(models.Manager):
    def create_validator(self, post_data):
        errors = {}
        if not post_data.get('species'):
            errors['species'] = "Species should not be blank"
        elif len(post_data['species']) <2:
            errors['species'] = "Species at least 2 characters"
        if not post_data.get('location'):
            errors['location'] = "Address should not be blank"
        elif len(post_data['location']) <5:
            errors['location'] = "Address at least 5 characters"
        if not post_data.get('date_found'):
            errors['date_found'] = "Date should not be blank"
        else:
            from datetime import date
            try: 
                from datetime import datetime
                d = datetime.strptime(post_data['date_found'], "%Y-%m-%d").date()
                if d > date.today():
                    errors['date_found'] = "Date cannot be in the future"
            except ValueError:
                errors['date_found'] = "Invalid date format. Please use YYYY-MM-DD."
        if post_data.get('zip_code'):
            if not re.match(r'^\d{5}$', post_data['zip_code']):
                errors['zip_code'] = "Zip code must be 5 digits"
            if post_data.get('notes') and len(post_data.get('notes')) >50:
                errors['notes'] = "Notes must be 50 characters"
        return errors
                

class Tree(models.Model):
    species = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_found = models.DateField()
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    mapped_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trees')
    visitors = models.ManyToManyField(User, related_name='visited_trees', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TreeManager()