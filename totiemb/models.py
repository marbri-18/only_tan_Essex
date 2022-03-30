from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Product(models.Model):    
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    maker = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    product_type = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    product_size = models.CharField(max_length=50, default="0 ml")
    product_price = models.CharField(max_length=50, default="£0.00")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Customer(models.Model):
    fname = models.CharField(max_length=100, default="")
    lname = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    telephone = models.CharField(max_length=100, default="")
    dob = models.DateField(default="")
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['lname']

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Session(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer")
    customer_name = models.CharField(max_length=100, default="")
    session_date_time = models.DateTimeField(auto_now_add=True)
    over_18_yrs = models.BooleanField(default=False)
    tandc_understood = models.BooleanField(default=False)

    class Meta:
        ordering = ['-session_date_time']

    def __str__(self):
        return self.customer_name

           
