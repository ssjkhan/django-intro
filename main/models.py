from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.TextField()
    love = models.IntegerField()
    hobbies = models.ManyToManyField("Food", on_delete=models.CASCADE)

    def __str__(self):
        return f"PK: {self.id} name: {self.name}"
        
class Food(models.Model):
    name = models.TextField()
    flavour = models.TextField()

    def __str__(self):
        return f"PK: {self.id} name: {self.name}:"
