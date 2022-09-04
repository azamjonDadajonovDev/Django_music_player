from django.db import models

# Create your models here.

class MusicPlayerModel(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    music = models.FileField(upload_to='musics')
    image = models.ImageField(upload_to='images')
