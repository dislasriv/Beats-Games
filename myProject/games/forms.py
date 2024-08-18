from django import forms 
from . import models

# little form for users to input the game ID fo a game they want registered
class igdbGameForm(forms.ModelForm):
    class Meta():
        model = models.Game
        fields = ['igdbId']