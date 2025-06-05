# _*_ coding: utf-8 -*-
from django.db import models

# Create your models here.

class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default="http://i.imgur.com/Ous4iGB.png")
    
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.name

class Product(models.Model):
    pmodel = models.ForeignKey(
        PModel, 
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="型號"
    )
    nickname = models.CharField(max_length=15, default="超值二手機")
    description = models.TextField(default="暫無說明")
    year = models.PositiveIntegerField(default=2016)
    price = models.PositiveIntegerField(default=0)
    store = models.ForeignKey(
        Store,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="商店",
        related_name="products"
    )
    
    def __str__(self):
        return self.nickname
    
class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default="暫無說明")
    url = models.URLField(default="http://i.imgur.com/Z230eeq.png")
    
    def __str__(self):
        return self.description
