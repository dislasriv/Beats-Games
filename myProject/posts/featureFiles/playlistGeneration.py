from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
import genericHelpers as genericHelpers
import spotifyHelpers as spotifyHelpers
import spotipy

from . import playlistGenerationHelpers
import html
import exceptions
from myProject import views as projectViews



# A collection of helper functions for the posts app
#scope that our spotify client/api instance will use

# TODO: Error handling
# REQUIRES: An HTTPRequest, playlist ID, and an instance of the Playlist model
# MODIFIES: An instance of Models.playlist
# EFFECTS: Creates and saves a new instance of .models.Playlist to the database.
#          returns None if failure, edited/new model if success.
def compilePlaylist(playlistId, playlistModel):

    try:
        # Used to freeze cause acess token had not been stored for user
        playlist = spotifyHelpers.spotify.playlist(playlistId) # --> Freeze occurs here
        # set fields
        playlistModel.title = playlist['name']
        # saves playlsit image to image field
        playlistModel.bannerUrl = playlist['images'][0]['url']
        playlistModel.caption = html.unescape(playlist['description'])
        playlistModel.slug = playlistGenerationHelpers.slugifyPlaylistNames(playlistModel)
        
        # Handles arrangement of songs
        playlistModel.songs = compilePlaylistSongs(playlist['tracks'])

        playlistModel.save()
        # returns model
        return playlistModel
    
    except spotipy.exceptions.SpotifyException as e:
        return None

# REQUIRES: A Playlist ImageFieldto be inputted as well as a valid URL (should always be valid and exist)
# MODIFIES: model
# EFFECTS: saves image to Playlist model's ImageField
def saveImageToPlaylistFromUrl(imageField, url, filename):
    imgDownload = genericHelpers.dowloadImageFromUri(url)
    imageField.save(filename, ContentFile(imgDownload))

# REQUIRES: A valid HTTP request, A playlist instance and a set of PROPERLY inputted ids as params
# MODIFIES: playlistInstance
# EFFECTS: Handles errors for assigning gameIds to playlist and making the proper associations
def handleGameIds(request, playlistInstance, gameIds):
    try:
       return playlistGenerationHelpers.associateGamesToPlaylist(playlistInstance, gameIds)

    # if input wrong throw error page
    except exceptions.FormInputFormatException as e:
        return projectViews.errorPage(request, "Game Id list was not properly formatted, please use a comma separated list with no spaces and only numeric characters")
    
    # if not all ids are on the database
    except ObjectDoesNotExist:
        return projectViews.errorPage(request, "Not all IGDB ids inputted were registered to beats&games.")


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

            # on the off chance some songs have been deleted  (not just deactivated) by spotify??
            if trackInfo == None:
                continue
            
            # handle episodes/songs differently
            if trackInfo['type'] == 'track':
                thisSong = {
                    #TODO: add song details
                    "name" : trackInfo['name'],
                    "artists" : playlistGenerationHelpers.createArtistArray(trackInfo),
                }
            else:
                print(trackInfo)
                print()
                
                # TODO: API reference for episodes is completely false, refer to objects returned to get data you want
                thisSong ={
                    "name" : trackInfo['name'],
                    "show" : trackInfo['artists'][0]['type'],
                }

                # append shared keys/values between TrackObjects and EpisodeObjects
                
            # check that an album image is present
            if(len(trackInfo['album']['images']) > 0):
                thisSong['imageurl'] = trackInfo['album']['images'][0]['url']
            # add type to dict
            thisSong['type'] = trackInfo['type']

            out.append(thisSong)

        # set the api result to the data at the next URL under the original API request's ['tracks'] dict
        # grabs ONLY the next 'tracks' array and assigns it to our var, keeping all of our dictionary paths valid.
        # This only works so long as the api_result we pass into next still has the 'next' key visible 
        # (ie: we havent cut) too far into the dict.
        # Spotify.next(current_api_result) works no matter your api result, so long as the JSON still has the
        # 'next' key visible.

        # our SPOTIFY API instance keeps track of which link (tracks) is next for a particular API call.
        api_result = spotifyHelpers.spotify.next(api_result)

    return out



