
from games.models import Game


# REQUIRES: a playlist model as input
# MODIFIES: out
# EFFECTS: for every gameId in a playlist's gameIds string, pull it from the DB
# INVARIANT: ALL ids are valid
def getGamesForPlaylist(playlistInstance):
    # if string empty return empty array.
    if len(playlistInstance.gameIds) == 0:
        return []
    
    # setup output
    out = []
    gameIds = playlistInstance.gameIds.split(',')

    # for every ID pull the game
    for gameId in gameIds:  
        # add the game object from the DB having this ID to the output
        out.append(Game.objects.get(igdbId=gameId))

    return out