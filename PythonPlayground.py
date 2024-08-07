import requests
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


scope = 'playlist-read-private'

def main():
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    
    try:
        playlist = spotify.playlist("20g1GYEqzeiD8IMpSMj21J")
        return playlist
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    main()

