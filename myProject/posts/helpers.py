import genericHelpers
import spotifyHelpers
import spotipy
from django.core.files.base import ContentFile

# A collection of helper functions for the posts app
#scope that our spotify client/api instance will use


# TODO: (this is just a note) the authorization code flow completely nukes the program and i have no idea
# why and it makes me want to expire like a can of tuna.

# REQUIRES: An HTTPRequest, playlist ID, and an instance of the Playlist model
# MODIFIES: An instance of Models.playlist
# EFFECTS: Creates and saves a new instance of .models.Playlist to the database.
#          returns false if failure, true if success.
def makePlaylistFromForm(playlistId, playlistModel):

    try:
        # Used to freeze cause acess token had not been stored for user
        playlist = spotifyHelpers.spotify.playlist(playlistId) # --> Freeze occurs here
        # set fields
        playlistModel.title = playlist['name']
        # saves playlsit image to image field
        saveImageToPlaylistFromUrl(playlistModel, playlist['images'][0]['url'])
        playlistModel.caption = playlist['description']
        playlistModel.slug =  genericHelpers.preprocessPlaylistNames(playlistModel.title)
        playlistModel.save()
        return True
    
    except spotipy.exceptions.SpotifyException as e:
        return False
    
# REQUIRES: A Playlist model to be inputted as well as a valid URL (should always be valid and exist)
# MODIFIES: model
# EFFECTS: saves image to Playlist model's ImageField
def saveImageToPlaylistFromUrl(model, url):
    imgDownload = genericHelpers.dowloadImageFromUri(url)
    model.banner.save(model.playlistId, ContentFile(imgDownload))

