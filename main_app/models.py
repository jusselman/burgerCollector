from django.db import models
from django.urls import reverse

# Create your models here.
class Burger(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    quality = models.IntegerField()
    
def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('detail', kwargs={'burger_id': self.id})

