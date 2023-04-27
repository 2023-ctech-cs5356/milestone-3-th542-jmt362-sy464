from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static

CATEGORIES = [
    ('appliances', 'Appliances'),
    ('clothes', 'Clothes'),
    ('education', 'Education'),
    ('electronics', 'Electronics'),
    ('free', 'Free'), 
    ('homeandgarden', 'Home & Garden'), 
    ('miscellaneous', 'Miscellaneous'),
    ('music', 'Music'),
    ('sports', 'Sports'),
    ('vehicles', 'Vehicles'), 
    ]

class Item(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 200)
    category = models.CharField(max_length = 20, choices = CATEGORIES, default = 'miscellaneous')
    price = models.DecimalField(max_digits = 15,decimal_places = 2)
    created = models.DateTimeField(auto_now_add = True)
    photo = models.ImageField(upload_to='images/', null = True, blank = True)
    description = models.TextField(default='No description provided.')
