from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        
        # First Name
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "الاسم الأول يجب أن يكون حرفين على الأقل"
        if not post_data['first_name'].isalpha():
            errors['first_name'] = "الاسم الأول يجب أن يحتوي على حروف فقط"
        
        # Last Name
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "اسم العائلة يجب أن يكون حرفين على الأقل"
        if not post_data['last_name'].isalpha():
            errors['last_name'] = "اسم العائلة يجب أن يحتوي على حروف فقط"
        
        # Email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "البريد الإلكتروني غير صالح"
        
        # Unique Email (NINJA BONUS)
        if User.objects.filter(email=post_data['email']).exists():
            errors['email_unique'] = "هذا البريد الإلكتروني مسجل مسبقاً"
        
        # Password
        if len(post_data['password']) < 8:
            errors['password'] = "كلمة المرور يجب أن تكون 8 أحرف على الأقل"
        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "كلمتا المرور غير متطابقتين"
        
        return errors
    
    def login_validator(self, post_data):
        errors = {}
        
        # Check email exists
        users = User.objects.filter(email=post_data['email'])
        if not users:
            errors['login'] = "البريد الإلكتروني أو كلمة المرور غير صحيحة"
            return errors
        
        # Check password
        user = users[0]
        if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
            errors['login'] = "البريد الإلكتروني أو كلمة المرور غير صحيحة"
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField(unique=True)
    password   = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
