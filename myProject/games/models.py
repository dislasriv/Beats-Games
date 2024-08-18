from django.db import models

# Create your models here.
class Game(models.Model):
    # IGDB id
    igdbId = models.CharField(max_length=100)
    # name from IGD request
    title = models.CharField(max_length=50)

    # https://images.igdb.com/igdb/image/upload/t_cover_big/{image_id}.jpg is the format of the link we want
    # where image_id comes from an IGDB request to https://api.igdb.com/v4/games
    coverUrl = models.TextField()

    # release date, fix into string via import datetime
    releaseYear = models.TextField()

    # how many playlists are associated to this game?
    associations = models.IntegerField()

    def __str__(self):
        return self.title;
