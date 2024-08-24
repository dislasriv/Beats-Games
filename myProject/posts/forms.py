from django import forms 
from . import models
from django.utils.safestring import mark_safe

class CreatePlaylist(forms.ModelForm):
    class Meta:
        model = models.Playlist
        fields = ['playlistId', 'description', 'gameIds']

# Form for customizing NON-SPOTIFY playlist data after model generation.
class EditPlaylist(forms.ModelForm):
    class Meta:
        model = models.Playlist
        fields = ['description','gameIds']
        help_texts= {
            'description': "Genres, artists, themes, why is this playlist great for the associated games?",
            'gameIds' : mark_safe('<ul><li>A comma separated list of ONLY ids seen on the games page.</li><li> please include only numeric characters with at most one comma between each.</li><ul>')
        }
       

  

