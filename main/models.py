from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

# blog model
class Blog(models.Model):
    title = models.CharField(default='', max_length=100)
    desc = RichTextField()
    author = models.CharField(default='harshraj8843', max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=True)

# contact model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    time = models.DateTimeField(auto_now=False, auto_now_add=True)