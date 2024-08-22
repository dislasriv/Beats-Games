import requests

# moved token to here since expiry takes a freaking long time (sessions will not be 57 days long)
token = requests.post("https://id.twitch.tv/oauth2/token?client_id=1f4zmb8fbzgrbslh2znny1tg1zfrxf&client_secret=kxromxpjrgdhu51fxljwjop9rwxtm5&grant_type=client_credentials").json()["access_token"]

# EFFECTS: grabs response from the IGDB games API endpoint (made to clean code)
def getGameById(igdbId):
   return requests.post('https://api.igdb.com/v4/games', **{'headers': {'Client-ID': '1f4zmb8fbzgrbslh2znny1tg1zfrxf', 'Authorization': "Bearer " + token, 'Content-Type': 'application/json'},'data': 'fields id, name, cover.image_id, first_release_date; where id =' + igdbId +';'}).json()