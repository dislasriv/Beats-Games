import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


# A collection of helper functions for the posts app
#scope that our spotify client/api instance will use
scope = 'playlist-read-private'

# REQUIRES: An HTTPRequest, playlist ID, and an instance of the Playlist model
# MODIFIES: An instance of Models.playlist
# EFFECTS: Creates and saves a new instance of .models.Playlist to the database.
#          returns false if failure, true if success.
def makePlaylistFromForm(playlistId, playlistModel):
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=""))

    try:
        # TODO: Program freezes at this function, starts randomly generating the home page, NO IDEA
        print(playlistId)
        playlist = spotify.playlist(playlistId)
        print("hi please help me")
        # set fields
        playlistModel.title = playlist['name']
        # will likely not work (url is a string)
        playlistModel.banner= playlist['images']['url']
        print("i oopsed")
        playlistModel.slug =  playlistModel.title.replace(" ", "-")
        playlistModel.save()
        return True
    
    except spotipy.exceptions.SpotifyException as e:
        print("the program has failedd")
        return False
    

if __name__ == "__main__":
    makePlaylistFromForm("20g1GYEqzeiD8IMpSMj21J", None)
    print("WHAT THE FUCK")