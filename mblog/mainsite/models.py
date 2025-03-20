from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)
    
    def __str__(self):
        return self.title

class Phone(models.Model):
    RAM_CHOICES = [
        ('2GB', '2GB'),
        ('4GB', '4GB'),
        ('6GB', '6GB'),
        ('8GB', '8GB'),
    ]
    
    ROM_CHOICES = [
        ('16GB', '16GB'),
        ('32GB', '32GB'),
        ('64GB', '64GB'),
        ('128GB', '128GB'),
    ]
    
    name = models.CharField(max_length=200)
    intro = models.TextField()
    ram = models.CharField(max_length=10, choices=RAM_CHOICES)
    rom = models.CharField(max_length=10, choices=ROM_CHOICES)
    price = models.IntegerField()
    image = models.CharField(max_length=500, blank=True, help_text="Enter a URL for the phone image")
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)
    
    def __str__(self):
        return self.name