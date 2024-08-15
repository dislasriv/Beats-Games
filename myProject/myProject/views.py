#from django.http import HttpResponse
from django.shortcuts import render, redirect

import spotipy
from spotipy import oauth2
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotifyHelpers

# login to spotify directly
def spotify_login(request):
    return redirect(spotifyHelpers.sp_oauth.get_authorize_url())

def spotify_callback(request):
    # get authorization code, from Django HTTP request
    code = request.GET.get('code')
    # get user access token from code
    token_info = spotifyHelpers.sp_oauth.get_access_token(code)
    # record token to prevent further sign in popups.
    request.session['token_info'] = token_info
    return redirect("/home/")

def homePage(request):
    #return HttpResponse("Hello World!")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("information about my page: creator is human waste!")
    return render(request, 'about.html')


# Views with no URL
def errorPage(request, message):
    return render(request, 'error.html', {'error':message})