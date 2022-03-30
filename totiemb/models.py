from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Products(models.Model):    
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    maker = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    product_type = models.CharField(max_length=100, blank=True)
    Description = models.TextField(blank=True)
    product_size = models.CharField(max_length=50, default="0 ml")
    product_price = models.CharField(max_length=50, default="£0.00")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
