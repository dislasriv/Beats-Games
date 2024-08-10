import spotipy
from spotipy import oauth2
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# Contains variables for link to spotify API, and some setup helpers

# spotify stuff
scope = 'playlist-read-private playlist-read-collaborative'

#instance of API
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='904a04b42c8c4af0a7af4a48dba10bfc',
    client_secret='f92075121ddd4f06a3ec8a7d4726173a',
    redirect_uri='http://localhost:8000/spotify_callback',
    scope=scope))
# oauth
sp_oauth = oauth2.SpotifyOAuth(client_id='904a04b42c8c4af0a7af4a48dba10bfc',
                                   client_secret='f92075121ddd4f06a3ec8a7d4726173a',
                                   redirect_uri='http://localhost:8000/spotify_callback',
                                   scope=scope)


