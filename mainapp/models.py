from pydoc import describe
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Food(models.Model):
    food_name = models.CharField(max_length=100, null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.food_name} {self.description}'
