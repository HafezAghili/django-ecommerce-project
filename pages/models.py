from django.db import models
from django.urls import reverse
from datetime import datetime , timedelta

import accounts.models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50 , blank=False , null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField(default=30)
    img = models.ImageField()
    quality = models.CharField(max_length= 50 , choices=[('high quality','high quality') ,
                                                         ('medium quality','medium quality') ,
                                                         ('low quality','low quality')])
    supplier = models.ManyToManyField('Supplier')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True) 
    expiration_at = models.DateField(default=datetime.now()+timedelta(days=730))

    def __str__(self):
        return f'{self.name} {self.city}'
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city
    

class Supplier(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False,choices=[('AbuAuf','AbuAuf'),
                                                                          ('Abgineh','Abgineh'),
                                                                          ('Anned','Anned'),
                                                                          ('Borroje','Borroje'),
                                                                          ('Diestro','Diestro')])
    contactInfo = models.CharField(max_length=50) 

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey('City' , on_delete=models.CASCADE)
    address = models.CharField(max_length=50) 
    phone = models.CharField(max_length=50) 

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class CartItem(models.Model):
    cart = models.ForeignKey('Cart' , on_delete=models.CASCADE)
    product = models.ForeignKey('Product' , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50 , default='Submitted' ,choices=[('Submitted','Submitted'),
                                                                            ('Ready to send','Ready to send'),
                                                                            ('Sent','Sent')])

    def __str__(self):
        return self.cart+' '+self.product
    

class Order(models.Model):
    user = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    

class OrderItem(models.Model):
    order = models.ForeignKey('Order' , on_delete=models.CASCADE)
    product = models.ForeignKey('Product' , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50 , default='Submitted' ,choices=[('Submitted','Submitted'),
                                                                            ('Ready to send','Ready to send'),
                                                                            ('Sent','Sent')])

    def __str__(self):
        return self.order+' '+self.product