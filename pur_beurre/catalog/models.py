"""model management"""
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    """Category table"""
    name = models.CharField(max_length=100)


class Product(models.Model):
    """Product table"""
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    brand = models.CharField(max_length=200)
    nutrition_grade = models.CharField(max_length=1)
    picture = models.URLField()
    nutrition_image = models.URLField()
    url = models.URLField()
    last_modified_t = models.DateField(null=True, blank=True)
    openff_id = models.BigIntegerField(null=True, blank=True)

class UserFavorite(models.Model):
    """UserFavorite table"""
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
