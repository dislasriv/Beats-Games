from django.urls import path
from . import views


app_name = "information"

urlpatterns = [
    path('tutorial-playlist', views.tutorial_playlist, name="tutorial-playlist"),
    path('tutorial-game', views.tutorial_game, name="tutorial-game"),
]