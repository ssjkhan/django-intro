from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.TextField()
    love = models.IntegerField()
    hobbies = models.ForeignKey("Hobby", on_delete=models.CASCADE)

    def __str__(self):
        return f"PK: {self.id} name: {self.name}"
        
class Hobby(models.Model):
    name = models.TextField()
    annual_cost = models.IntegerField()

    def __str__(self):
        return f"PK: {self.id} name: {self.name}:"
