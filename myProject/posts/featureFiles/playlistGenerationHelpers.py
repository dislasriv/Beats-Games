import exceptions
from games.models import Game

# REQUIRES: a posts.Playlist model
# MODIFIES: an output string
# EFFECTS: replaces problematic characters that can be misinterpreted from playlist slugs
#          with empty spaces, converts space chars to -, adds playlist ID at end of slug.
def slugifyPlaylistNames(playModel):
    # TODO: could abstract the removing problematic chars part
    playName = playModel.title
    illegalChars = ['!','@','#','$','%','^', '&','*','(',')', '+','`','\\',':',';','/','?','"', ' ']

    for char in illegalChars:
       playName = playName.replace(char, "")

    return playName.replace(" ", "-") + playModel.playlistId

# REQUIRES: A trackObejct array (see API)
# MODIFIES: out array
# EFFECTS: Comiples a JSON string with the names of all artists in the order that trackInfo has them in
def createArtistArray(trackInfo):
    out="("
    for artistJSON in trackInfo['artists']:
        out += artistJSON['name'] + ", "
    # notation to cut off last two chars (substring)
    return out[:-2] + ")"


# REQUIRES: A playlist instance and a set of PROPERLY inputted ids as params
# MODIFIES: playlistInstance
# EFFECTS: if string correctly formatted
    #          For every game currently in the playlistInstance's gameIds string, remove assoication, 
    #          for every game in the new string add association.
    #          if at any point id is invalid throw that as error
    #       else 
    #           throw error
def associateGamesToPlaylist(playlistInstance, idString): 
# INPUT VALIDATION SECTION
    legalChars = '1234567890,'
    # account for spaces
    idString = idString.replace(" ", "")

    # check that all chars are numeric or comma, ie: correct formatting
    for i in range(len(idString)):
        # get char
        char = idString[i]

        # check if final char is not comma, if it is cut it
        if i == len(idString)-1 and idString[i] == ',':
            idString = idString[:-1]

        if char not in legalChars:
            raise exceptions.FormInputFormatException("Invalid idString")
    
    # if format is correct, remove duplicates and check that length is <= 12
    currentGameIds = set(idString.split(","))
    if len(currentGameIds) > 12:
        raise exceptions.TooManyAssociatedGamesToPlaylist("too many games")
    
# INPUT PROCESSING SECTION
    # then for every id inputted (if any) add one association
    if len(idString) > 0:
        games = []
        for gameId in currentGameIds:
            games.append(Game.objects.get(igdbId=gameId))

        # in order to remove dupes from idString
        idString = ''
        # after confirming that all games exist add a new association and push to the DB
        for game in games:
            # reset idString
            idString += game.igdbId+","
            game.associations += 1
            game.save()
        # take last comma away
        idString = idString[:-1]
    print(playlistInstance.gameIds)

    # for every game id the player currently has associated, if any, reduce one association
    if len(playlistInstance.gameIds) > 0:
        # for every game id the player currently has associated, reduce one association
        currentGameIds = playlistInstance.gameIds.split(",")
        for gameId in currentGameIds:
            thisGame = Game.objects.get(igdbId=gameId)
            thisGame.associations -= 1
            # push to DB
            thisGame.save()
    
    # update field
    playlistInstance.gameIds=idString
    return playlistInstance
