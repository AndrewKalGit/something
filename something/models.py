from django.db import models
from django.forms import CharField

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    company_site = models.TextField()
    location = models.CharField(max_length=100)


class Cars(models.Model):
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    make = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='cars')
