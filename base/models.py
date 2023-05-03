from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static

CATEGORIES = [
    ('Appliances', 'Appliances'),
    ('Clothes', 'Clothes'),
    ('Education', 'Education'),
    ('Electronics', 'Electronics'),
    ('Free', 'Free'), 
    ('Home & Garden', 'Home & Garden'), 
    ('Miscellaneous', 'Miscellaneous'),
    ('Music', 'Music'),
    ('Sports', 'Sports'),
    ('Vehicles', 'Vehicles'), 
    ]

class Item(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 200)
    contact =  models.CharField(max_length = 50)
    category = models.CharField(max_length = 20, choices = CATEGORIES, default = 'Miscellaneous')
    price = models.DecimalField(max_digits = 15, decimal_places = 2)
    created = models.DateTimeField(auto_now_add = True)
    photo = models.ImageField(upload_to='images/', null = True, blank = True)
    description = models.TextField(default='No description provided.')
