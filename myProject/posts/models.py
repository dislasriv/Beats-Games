from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Playlist(models.Model):
    # Fields taken from Spotify API callback.
    title = models.CharField(max_length=50)
    # The spotify playlist bio.
    caption = models.TextField()

    # Why its good for X game.
    description = models.TextField(default="Why is this playlist awesome for this game?")
    bannerUrl = models.TextField(default = "if youre seeing this there is an error, start at posts/models.py")
    playlistId = models.CharField(max_length=200, default = "")

    #static fields
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = None)

    # dictionary with all songs (in dictionary format) organized.
    songs = models.JSONField(default=dict)

    # Comma separated string of gameIds (with NO SPACES) that this playlist is associated with
    gameIds = models.TextField(default="")

    def __str__(self):
        return self.title

