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
      (2, 'liter'),
    )
    name = models.CharField(max_length=255,unique=True)
    quantity = models.IntegerField()
    unit = models.IntegerField(choices=UNIT_CHOICES)
    price = models.FloatField()