from django.shortcuts import render

# Create your views here.

# EFFECTS: Render info page
def tutorial_playlist(request):
    return render(request, "information/tutorial_playlist.html")

# EFFECTS: Render info page
def tutorial_game(request):
    return render(request, "information/tutorial_game.html")