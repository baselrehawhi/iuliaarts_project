from django.db import models
from datetime import datetime
import datetime
from django.utils import timezone


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    
def __str__(self):
    return self.name