from django.db import models
from django.contrib.auth.models import AbstractUser
import jsonfield


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
    quantity = models.IntegerField(null=True, blank=True, default=0)
    unit = models.IntegerField(choices=UNIT_CHOICES, null=True, blank=True, default=None)
    price = models.FloatField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=255,unique=True)
    quantity = models.IntegerField(blank=True, null=True, default=None)
    selling_price = models.FloatField(blank=True, null=True, default=0)
    cost_price = models.FloatField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class IngredientProduct(models.Model):
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, default=None, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderDetails(models.Model):
    customer = models.CharField(max_length=255, default=None, null=True, blank=True)
    grand_total = models.FloatField(default=0, null=True, blank=True)
    products = jsonfield.JSONField(blank=True, default=[], null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
