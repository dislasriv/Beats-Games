from django import forms 
from . import models

class CreatePlaylist(forms.ModelForm):
    class Meta:
        model = models.Playlist
        fields = ['playlistId', 'description']

# Form for customizing NON-SPOTIFY playlist data after model generation.
class EditPlaylist(forms.ModelForm):
    class Meta:
        model = models.Playlist
        # Include only editable fields
        fields = ['description']
