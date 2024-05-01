from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    last_update = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.URLField()
    last_update = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

class Tracks(models.Model):
    title = models.CharField(max_length=100)
    cover = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)


