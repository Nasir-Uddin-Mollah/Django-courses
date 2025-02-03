from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.CharField(default='Karim', max_length=100)

    def __str__(self):
        return f"{self.roll}-{self.name}"
