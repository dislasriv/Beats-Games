

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