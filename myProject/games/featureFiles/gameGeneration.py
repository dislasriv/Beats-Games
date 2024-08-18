import requests
import genericHelpers

# REQUIRES: a STRING input (id) and an instance of the Game model as params.
# MODIFIES: gameModel.
# EFFECTS: fills out/refreshes the fields for the gameModel and pushes the changes/new game to the DB.
def compileGame(igdbId, gameModel):
    # get access token
    token = requests.post("https://id.twitch.tv/oauth2/token?client_id=1f4zmb8fbzgrbslh2znny1tg1zfrxf&client_secret=kxromxpjrgdhu51fxljwjop9rwxtm5&grant_type=client_credentials").json()["access_token"]

    # perform request to API to get game data
    gameResponse = requests.post('https://api.igdb.com/v4/games', **{'headers': {'Client-ID': '1f4zmb8fbzgrbslh2znny1tg1zfrxf', 'Authorization': "Bearer " + token, 'Content-Type': 'application/json'},'data': 'fields id, name, cover.image_id, first_release_date; where id =' + igdbId +';'}).json()

    # if ID is invalid one of the two following cases will proc
    if len(gameResponse) != 1 or not "name" in gameResponse[0]:
        return None
    
    # else process and save the game to db!
    gameModel.title = gameResponse[0]['name']
    # get image using t_cover_big url and the image_id from IGDB
    gameModel.coverUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/" + gameResponse[0]['cover']['image_id'] + ".jpg"
    # get time from unixtimestamp first_relase_date 
    gameModel.releaseYear = genericHelpers.unixtimeToDate(gameResponse[0]['first_release_date']).strftime("%Y")
    # init associations field
    gameModel.associations = 0
    gameModel.save()
    return gameModel