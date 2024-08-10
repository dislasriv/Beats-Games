import genericHelpers
import spotifyHelpers
import spotipy
from django.core.files.base import ContentFile
from . import playlistGenerationHelpers

# A collection of helper functions for the posts app
#scope that our spotify client/api instance will use

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
        playlistModel.slug = playlistGenerationHelpers.slugifyPlaylistNames(playlistModel)
        # Handles arrangement of songs
        playlistModel.songs = compilePlaylistSongs(playlist['tracks'])
       
        # saves model to db
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


# REQUIRES: a spotify playlist returned by the API in JSON format.
# MODIFIES: an array of dictionaries where each element is a song on a playlist, and each subelement is 
#           an attribute of a song (ie: name).
# EFFECTS: for each song creates a dictionary to represent its attributes and stores it in an array
def compilePlaylistSongs(api_result):
    out = []

    # for every 'item' in our JSON, parse it into relevant data.
    while(api_result != None):
        for itemJSON in api_result['items']:

            # See API (get playlist section) for data inside each item dictionary, 
            # the stuff inside the 'track' dict is what we want.
            trackInfo = itemJSON['track']

            thisSong = {
                #TODO: add song details
                "name" : trackInfo['name'],
            }
            out.append(thisSong)

        # set the api result to the data at the next URL under the original API request's ['tracks'] dict
        # grabs ONLY the next 'tracks' array and assigns it to our var, keeping all of our dictionary paths valid.
        # This only works so long as the api_result we pass into next still has the 'next' key visible 
        # (ie: we havent cut) too far into the dict.
        # Spotify.next(current_api_result) works no matter your api result, so long as the JSON still has the
        # 'next' key visible.

        # our SPOTIFY API instance keeps track of which link is next for a particular API call.
        api_result = spotifyHelpers.spotify.next(api_result)

    return out



