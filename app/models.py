from django.db import models
from django.utils import timezone
# Create your models here.

class audioStore(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    file = models.FileField(null = True, blank = True)

