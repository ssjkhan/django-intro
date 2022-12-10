from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.TextField(blank=False)
    favFoods = models.ManyToManyField("Food")

    def __str__(self):
        return f"PK: {self.id} name: {self.name}"
        
class Food(models.Model):
    name = models.TextField()
    flavour = models.TextField()

    def __str__(self):
        return f"PK: {self.id} name: {self.name}:"
