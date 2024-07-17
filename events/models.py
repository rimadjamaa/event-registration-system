from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.text import slugify

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField(default=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name

