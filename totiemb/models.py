from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "draft"), (1, "published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
