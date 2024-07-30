from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
    return render(request, 'posts/posts_list.html', {'posts':Post.objects.all().order_by("-date")})
