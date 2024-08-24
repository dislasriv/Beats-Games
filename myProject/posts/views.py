from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# working dir imports
from .featureFiles import playlistGeneration
from .models import Playlist
from . import forms
from .featureFiles import playlistGeneration
from .featureFiles import generalPlaylistHelpers 

# project imports
import myProject.views as views

# games app imports
from games.models import Game

# Note: posts_lists.html is an abstract HTML file for rendering all lists of posts, give a list of posts to render
#       and a heading.
# post list pages.
def posts_list(request):
    return render(request, 'posts/posts_list.html', {'posts':Playlist.objects.all().order_by("-date"),
                                                     'heading':"Recent playlists"})
# render only the posts made by the current user

@login_required(login_url="/users/login/")
def user_posts_list(request):
    return render(request, 'posts/posts_list.html', {'posts':Playlist.objects.filter(author=request.user),
                                                     'heading': "Your playlists"})

# render only the posts having the relevant gameId in their list.
# INVARIANT: if this function is called the id is valid.
def game_posts_list(request, gameId):
    game = Game.objects.get(igdbId=gameId)
    return render(request, 'posts/posts_list.html', {'posts':Playlist.objects.filter(gameIds__contains=gameId),
                                                     'heading': "Playlists for " + game.title + " (" +game.releaseYear+")",
                                                     'banner': game.coverUrl},)

# other pages
# TODO: bug, this shit runs twice??
def post_page(request, slug):
    # get old post just to fish ID (this will never change)
    post = Playlist.objects.get(slug=slug)
    # refresh and compile playlist, 
    post = playlistGeneration.compilePlaylist(post.playlistId, post)
    #get post with particular slug, send it as the post we want to represent in the post template
    return render(request, 'posts/post_page.html',{'this_post':post,
                                                   'games': generalPlaylistHelpers.getGamesForPlaylist(post)})


@login_required(login_url="/users/login/")
# INVARIANT: user owns playlist when this view is activated
def edit_post(request, playlistId):
    # if doesnt own playlist send to banworld
    playlistEditing = Playlist.objects.get(playlistId=playlistId)
    
    if request.method == 'POST':
        # TODO: if any file uploads are added to the form, add a request.FILES arg
        form = forms.EditPlaylist(request.POST)

        if form.is_valid():
            # save form data TODO: maybe pacakge into helper
            tempPlaylist = form.save(commit=False)
            # update fields,more when more complex fields are made
            playlistEditing.description = tempPlaylist.description

            # set associations to games that the user is trying to assign to their playlist
            # if funtion fails newPLaylist will be an HTTPResponse 
            playlistEditing = playlistGeneration.handleGameIds(request, playlistEditing, tempPlaylist.gameIds)
            if isinstance(playlistEditing, HttpResponse):
                return playlistEditing

            # update post on DB
            playlistEditing.save()
            # reload post
            return redirect('/posts/' + playlistEditing.slug)

    else:
        # indicate that we are editing an instance to populate the fields by default, via the kwarg INSTANCE
        form = forms.EditPlaylist(instance=playlistEditing)
    return render(request, "posts/edit_post.html", {'form':form,
                                                    'playlistId':playlistId,
                                                    'slug':playlistEditing.slug})


@login_required(login_url="/users/login/")
def new_post(request):
    if request.method == 'POST':
        form = forms.CreatePlaylist(request.POST, request.FILES)

        if form.is_valid():
            #save playlist
            newPlaylist = form.save(commit=False)

            # check that this playlist hasn't already been posted, if the try proceeds send to the error page.
            try:
                Playlist.objects.all().get(playlistId=newPlaylist.playlistId)
                return views.errorPage(request, "This playlist has already been uploaded!")
            except:
                # do nothing, everything is working
                pass    
            # else set it all up and post the playlist
            newPlaylist.author = request.user
            
            # Keep gameId input but clear the field since handleGameIds assumes new playlists have an empty
            # gameIds string and its behaviour is not defined for a form.save object.
            gameIdString = newPlaylist.gameIds
            newPlaylist.gameIds = ''

            # set associations to games based on games the user wants to associate to the game
            # if funtion fails newPLaylist will be an HTTPResponse 
            newPlaylist = playlistGeneration.handleGameIds(request, newPlaylist, gameIdString)
            if isinstance(newPlaylist, HttpResponse):
                return newPlaylist

            # call helper function that returns new playlist model object
            compPlaylist = playlistGeneration.compilePlaylist(newPlaylist.playlistId, newPlaylist)

            # if complilation of playlist went okay redirect to posts
            if compPlaylist != None:
                # Push to the DB
                return redirect('/posts/')
            
            # else refresh page
            return views.errorPage(request, "Playlist id was invalid or something went wrong with the Spotify API")
    else: 
        form = forms.CreatePlaylist()
    return render(request, 'posts/new_post.html', {'form':form})

@login_required(login_url="/users/login/")
# INVARIANT: user owns playlist when this view is activated
def delete_post(request, playlistId):
   
   if request.method == 'POST':
        playlist = Playlist.objects.get(playlistId=playlistId)
        if request.POST.get('decision', 'no') == 'yes':
            playlist = Playlist.objects.get(playlistId=playlistId)
            playlist.delete()
            return redirect('posts:user-list')
        else:
            # redirect pack to post c:
            print(request.POST.get('decision', 'no'))
            return redirect('posts:page', slug=playlist.slug)
   else:   
        return render(request, "posts/delete_post.html", {'playlistId': playlistId})