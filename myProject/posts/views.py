from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
    return render(request, 'posts/posts_list.html', {'posts':Post.objects.all().order_by("-date")})


def post_page(request, slug):
    posts = Post.objects.all().order_by("-date")
    #get post with particular slug, send it as the post we want to represent in the post template
    return render(request, 'posts/post_page.html',{"this_post":posts.get(slug=slug),})
