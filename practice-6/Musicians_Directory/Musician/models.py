from django.db import models

# Create your models here.


class MusicianModel(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=15)
    Instraument_Type = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"