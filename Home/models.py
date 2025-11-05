from django.db import models
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=12)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.datetime.now())