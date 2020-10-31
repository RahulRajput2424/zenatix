from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(db_index=True, unique=True)
    mobileNumber = models.CharField(null=True,max_length=18, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Ingredient(models.Model):
    UNIT_CHOICES = (
      (1, 'kg'),
    )
    name = models.CharField(max_length=255,unique=True)
    quantity = models.IntegerField()
    unit = models.IntegerField(choices=UNIT_CHOICES,default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)