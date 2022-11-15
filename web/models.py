from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title = models.TextField()
    # image = models.ImageField()
    
  

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.TextField()
    image = models.ImageField()
    unit = models.IntegerField()
    price = models. IntegerField()
    discount = models.IntegerField()
    

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length = 50)
    email = models.CharField(max_length= 50)
    phone = models.IntegerField()

    def __str__(self):
        return self.customer_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
