""" Showing tables in the admin part """
from django.contrib import admin
from .models import Product, Category, UserFavorite

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(UserFavorite)
