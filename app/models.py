from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brands/')

    def __str__(self):
        return self.name    

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    # brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.id} - {self.title} "  

    
    
class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10,decimal_places=2)
    user = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.qty} - {self.sub_total}"
        

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
class Order(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    note = models.TextField( )
    user = models.ManyToManyField(User, null=True, blank=True)
    order_price = models.DecimalField( max_digits=8,decimal_places=2, null=True, blank=True) 
        