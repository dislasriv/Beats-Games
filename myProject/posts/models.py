from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Playlist(models.Model):
    # Fields taken from Spotify API callback.
    title = models.CharField(max_length=50)
    # The spotify playlist bio.
    caption = models.CharField(max_length=50, default = "")
    # Why its good for X game.
    description = models.TextField(default="Why is this playlist awesome for this game?")
    banner = models.ImageField(default="fallback.jpg", blank=True)
    playlistId = models.CharField(max_length=200, default = "")

    #static fields
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return "Post ToString:" + self.title

