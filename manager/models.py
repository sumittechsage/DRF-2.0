from django.db import models
from . import managers

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

    # no need to makemigrations if we change it 
    vidhyarthi = models.Manager() 
    students =  managers.CustomManager()

    def __str__(self):
        return self.name