import datetime
from django.db import models
from django.core.validators import MinValueValidator


class Brand(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    company = models.CharField(max_length=225, null=False, blank=False)


class Category(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    subs = models.ManyToManyField('SubCategory', related_name='subs_category', null=True, blank=True)


class SubCategory(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)


class BaseProduct(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    price = models.IntegerField(validators=[MinValueValidator(1000)])
    numbers = models.IntegerField(validators=[MinValueValidator(0)])
    create_date = models.TimeField(auto_now_add=True)
    # protect bc I think we can not have a product without brand or category
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, related_name='product_brand')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='product_category')


class ProductNumberOne(BaseProduct):
    something_extra = models.CharField(max_length=225, null=True, blank=True)


class ProductNumberTwo(BaseProduct):
    something_extra = models.CharField(max_length=225, null=True, blank=True)


class ProductNumberThree(BaseProduct):
    something_extra = models.CharField(max_length=225, null=True, blank=True)
