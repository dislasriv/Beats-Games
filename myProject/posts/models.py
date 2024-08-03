from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="fallback.jpg", blank=True)
   

    def __str__(self):
        return "Post ToString:" + self.title

