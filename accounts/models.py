from django.db import models
from pages.models import City , Cart
from django.contrib.auth.models import AbstractUser 
from django.core.validators import RegexValidator

# Create your models here.

class CustomUser(AbstractUser):
    city = models.ForeignKey(City, null=True, blank=False ,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    phone_regex  = RegexValidator(regex=r'^\+?98?\d{9,15}$', message="Phone number must be entered in the format: '+989123456789'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True , default="+989123456789") # Validators should be a list 

    def __str__(self):
        return self.username