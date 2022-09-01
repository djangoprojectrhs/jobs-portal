from django.db import models

# Create your models here.
class hydjobs(models.Model):
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)

class bangalorejobs(models.Model):
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
