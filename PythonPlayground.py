import requests
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


scope = 'playlist-read-private'

def main():
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='904a04b42c8c4af0a7af4a48dba10bfc',
        client_secret='f92075121ddd4f06a3ec8a7d4726173a',
        redirect_uri='http://localhost:8000/home',
        scope=scope))
    
    try:
        print("fuck")
        playlist = spotify.playlist("20g1GYEqzeiD8IMpSMj21J")
        print(playlist)
        return playlist
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    main()

