from django.db import models
# from cloudinary.models import CloudinaryField
# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)