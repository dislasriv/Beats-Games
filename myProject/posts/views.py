from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def posts_list(request):
    return render(request, 'posts/posts_list.html', {'posts':Post.objects.all().order_by("-date")})


def post_page(request, slug):
    posts = Post.objects.all().order_by("-date")
    #get post with particular slug, send it as the post we want to represent in the post template
    return render(request, 'posts/post_page.html',{"this_post":posts.get(slug=slug),})


@login_required(login_url="/users/login/")
def new_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)

        if form.is_valid():
            #save post
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('/posts/')
    else: 
        form = forms.CreatePost()
    return render(request, 'posts/new_post.html', {'form':form})
