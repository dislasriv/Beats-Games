from django.shortcuts import render, redirect
from .models import Game
from . import forms
from .featureFiles import gameGeneration
from django.contrib.auth.decorators import login_required
import myProject.views as projectWideViews

# Create your views here.

# render list of all games
def games_list(request):
    return render(request, "games/games_list.html", {"games": Game.objects.all().order_by("-associations")})

@login_required(login_url="/users/login/")
# EFFECTS: register a new game to the DB when method is POST, else render new game page.
def new_game(request):
    if request.method == "POST":
        # make an instance of the form with the info from request.POST in it
        form = forms.igdbGameForm(request.POST)

        # no errors with form
        if form.is_valid():
            # make instance from form
            newGame = form.save(commit=False)

             # check that this game isnt already up, if the try proceeds send to the error page.
            try:
                Game.objects.all().get(igdbId=newGame.igdbId)
                return projectWideViews.errorPage(request, "This game has already been registered!")
            except:
                # do nothing, everything is working
                pass

            # fill out fields by getting IGDB API data
            newGame = gameGeneration.compileGame(newGame.igdbId, newGame)

            if newGame == None:
                return projectWideViews.errorPage(request, "The game's ID was not valid.")
            return redirect('/games/')
        
    else:
        form = forms.igdbGameForm()
    return render(request, "games/new_game.html", {"form": form})