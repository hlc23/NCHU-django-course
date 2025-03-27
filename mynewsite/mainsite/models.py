from django.db import models

# Create your models here.

class Product(models.Model):
    item_number = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    SIZE = (
        ('small', 'small'),
        ('medium', 'medium'),
        ('large', 'large')
    )
    size = models.CharField(
        max_length=10,
        choices=SIZE,
        default='medium',
        null=False
    )

    def __str__(self):
        return f"{self.item_number}: {self.brand_name}"
    
    class Meta():
        ordering = ("-item_number",)