import requests
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

from requests import post

# code to get and refresh access
token = post("https://id.twitch.tv/oauth2/token?client_id=1f4zmb8fbzgrbslh2znny1tg1zfrxf&client_secret=kxromxpjrgdhu51fxljwjop9rwxtm5&grant_type=client_credentials").json()

print()
response = post('https://api.igdb.com/v4/games', **{'headers': {'Client-ID': '1f4zmb8fbzgrbslh2znny1tg1zfrxf', 'Authorization': "Bearer " + token['access_token'], 'Content-Type': 'application/json'},'data': 'fields id, name, artworks, cover.image_id, genres.name, platforms.name, summary; where id = 124333;'})

response = post('https://api.igdb.com/v4/artworks', **{'headers': {'Client-ID': '1f4zmb8fbzgrbslh2znny1tg1zfrxf', 'Authorization': "Bearer " + token['access_token'], 'Content-Type': 'application/json'},'data': 'fields id, image_id; where id = 28153;'})

print ("response: %s" % str(response.json()))

