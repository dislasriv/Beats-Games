import requests
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

from requests import post

# code to get and refresh access
token = post("https://id.twitch.tv/oauth2/token?client_id=1f4zmb8fbzgrbslh2znny1tg1zfrxf&client_secret=kxromxpjrgdhu51fxljwjop9rwxtm5&grant_type=client_credentials").json()

print()
response = post('https://api.igdb.com/v4/games', **{'headers': {'Client-ID': '1f4zmb8fbzgrbslh2znny1tg1zfrxf', 'Authorization': "Bearer " + token['access_token'], 'Content-Type': 'application/json'},'data': 'fields id, name, cover.image_id, first_release_date; where id = 621;'}).json()



print ("response: %s" % str(response))

