import requests
import genericHelpers as genericHelpers
from . import igdbHelpers

# REQUIRES: a STRING input (id) and an instance of the Game model as params.
# MODIFIES: gameModel.
# EFFECTS: fills out/refreshes the fields for the gameModel and pushes the changes/new game to the DB.
def compileGame(igdbId, gameModel):
    # perform request to API to get game data
    gameResponse = igdbHelpers.getGameById(igdbId)

    # if ID is invalid one of the two following cases will proc
    if len(gameResponse) != 1 or not "name" in gameResponse[0]:
        return None
    
    # else process and save the game to db!
    gameModel.title = gameResponse[0]['name']

    # get image using t_cover_big url and the image_id from IGDB
    # not all games have cover imgs so try-catch
    try:
        gameModel.coverUrl = "https://images.igdb.com/igdb/image/upload/t_cover_big/" + gameResponse[0]['cover']['image_id'] + ".jpg"
    except:
        # set to content unavailable image
        gameModel.coverUrl = "https://media.tenor.com/NpZyGNG3SLEAAAAM/this-content-is-not-available.gif"
        

    # get time from unixtimestamp first_relase_date 
    # not all games have relase years so try-catch
    try:
        gameModel.releaseYear = genericHelpers.unixtimeToDate(gameResponse[0]['first_release_date']).strftime("%Y")
    except:
        # leave NULL
        pass

    # init associations field
    gameModel.associations = 0
    gameModel.save()
    return gameModel