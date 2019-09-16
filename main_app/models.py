from django.db import models

# Create your models here.
class Burger(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    quality = models.IntegerField()
    



# class Photo(models.Model):
#     url = models.CharField(max_length=200)
#     burger = models.ForeignKey(Burger, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Photo for burger_id: {self.burger_id} @{self.url}"