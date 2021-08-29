from django.db import models
from datetime import datetime


# Create your models here.

class Pages(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.title
