from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Ninja(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)