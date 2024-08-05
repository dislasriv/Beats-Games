from django import forms 
from . import models

class CreatePlaylist(forms.ModelForm):
    class Meta:
        model = models.Playlist
        fields = ['title','body','banner']