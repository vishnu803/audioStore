from django.db import models
from django.utils import timezone
# Create your models here.

class audioStore(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    file = models.FileField(null = True, blank = True)
# class farmer(models.Model):
#     phone_no = models.CharField(max_length = 20, null = False, blank = False)
#     name = models.CharField(max_length = 50, null = True, blank = True)
#     location = models.CharField(max_length = 10, null = True, blank = True)

# class tokenStore(models.Model):
#     phone_no = models.OneToOneField(farmer, on_delete = models.CASCADE, null = False, blank = False)
#     token = models.CharField(max_length = 200, null = False, blank = False)
