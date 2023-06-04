from django.db import models
from pages.models import City
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class CustomUser(AbstractUser):
    city = models.ForeignKey(City, on_delete=models.CASCADE)