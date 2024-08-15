from django.shortcuts import render, redirect
from .featureFiles import playlistGeneration
from .models import Playlist
from django.contrib.auth.decorators import login_required
from . import forms
from .featureFiles import playlistGeneration


# Create your views here.
def posts_list(request):
    return render(request, 'posts/posts_list.html', {'posts':Playlist.objects.all().order_by("-date")})


def post_page(request, slug):
    post = Playlist.objects.all().order_by("-date").get(slug=slug)
    # refresh and compile playlist
    post = playlistGeneration.compilePlaylist(post.playlistId, post)
    #get post with particular slug, send it as the post we want to represent in the post template
    return render(request, 'posts/post_page.html',{"this_post":post,})


@login_required(login_url="/users/login/")
def new_post(request):
    if request.method == 'POST':
        form = forms.CreatePlaylist(request.POST, request.FILES)

        if form.is_valid():
            #save playlist
            newPlaylist = form.save(commit=False)

            # check that this playlist hasn't already been posted
            if(Playlist.objects.all().get(playlistId=newPlaylist.playlistId)):
                return redirect('/posts/new-post')
            # else set it all up and post the playlist
            newPlaylist.author = request.user
            # call helper function that returns new playlist model object
            compPlaylist = playlistGeneration.compilePlaylist(newPlaylist.playlistId, newPlaylist)

            # if complilation of playlist went okay redirect to posts, else TODO: redirect to error page
            if compPlaylist != None:
                # Push to the DB
                compPlaylist.save()
                return redirect('/posts/')
            # else refresh page
            return redirect('/posts/new-post')
    else: 
        form = forms.CreatePlaylist()
    return render(request, 'posts/new_post.html', {'form':form})
