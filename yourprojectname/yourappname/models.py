# models.py
from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class Size(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category=models.CharField(max_length=255 , default='')
    subcategory=models.CharField(max_length=255 ,default='')
    description = models.TextField()
    newprice = models.DecimalField(max_digits=10, decimal_places=2)
    oldprice = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='product_images/', null=True)  # Specify the upload_to path as needed
    def __str__(self):
        return self.name


class ProductColor(models.Model):
    colors = models.ForeignKey(Color, related_name='products',on_delete=models.CASCADE)
    products = models.ForeignKey(Product, related_name='colors',on_delete=models.CASCADE)


class ProductSize(models.Model):
    sizes = models.ForeignKey(Size, related_name='products',on_delete=models.CASCADE)
    products = models.ForeignKey(Product, related_name='sizes',on_delete=models.CASCADE)


class Order(models.Model):
    customer_name = models.CharField(max_length=255, default='admin')
    adress = models.CharField(max_length=255, default=0)
    phone= models.CharField(max_length=255, default=0)
    product_name = models.CharField(max_length=255, default=0)
    quantity = models.IntegerField( default=0)
    color = models.CharField(max_length=255, default=0)
    size = models.CharField(max_length=255, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"{self.customer_name} - {self.product_name}"
    


class Message(models.Model):
    name = models.CharField(max_length=255, default='admin')
    contact = models.CharField(max_length=255, default=0)
    message = models.CharField(max_length=1000, default=0)
    def __str__(self):
        return self.name