from django.db import models

# Create your models here.
class User(models.Model):
    username = models.fields.TextField(max_length=30)
    email = models.fields.TextField(max_length=30, unique=True)
    password = models.fields.TextField(max_length=30)
    is_active = models.fields.BooleanField(default=True)