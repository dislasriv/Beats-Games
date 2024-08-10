

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