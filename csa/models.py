from django.db import models
from django.db.models import query

# Create your models here.

class CustomerEnquiry(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    queries = models.CharField(max_length=500)
