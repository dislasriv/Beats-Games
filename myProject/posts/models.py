from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Playlist(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    title = models.CharField(max_length=50)
    body = models.TextField()
    banner = models.ImageField(default="fallback.jpg", blank=True)

    #static fields
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return "Post ToString:" + self.title

