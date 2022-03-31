from django.db import models

# Create your models here.
class Story(models.Model):
    fileName = models.CharField(max_length=200)