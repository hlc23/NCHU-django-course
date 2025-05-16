from django.db import models

# Create your models here.

class Mood(models.Model):
    status = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return self.status
    
class Post(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, default="Someone")
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=20)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    birth_year = models.IntegerField(null=True)
    topic = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.message