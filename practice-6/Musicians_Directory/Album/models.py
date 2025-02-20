from django.db import models
from Musician.models import MusicianModel
# Create your models here.


class AlbumModel(models.Model):
    Album_Name = models.CharField(max_length=100)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    Release_Date = models.DateField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    
    def __str__(self):
        return self.Album_Name