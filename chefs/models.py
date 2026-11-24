from django.db import models
from datetime import time


# Create your models here.
class Chef(models.Model):
    name = models.CharField(max_length=200)
    portrait = models.ImageField(upload_to="photos/%Y/%m/%d")
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
