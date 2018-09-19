from django.db import models

# Create your models here.

class Album(model.Model):
    artist =  models.CharField(max_length=250)
    album_title =  models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
