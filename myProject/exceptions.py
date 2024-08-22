

# exception handling tree for the project

# when form input is not as expected
class FormInputFormatException(Exception):
    pass

# when too many games are attempted to be associated to a playlist
class TooManyAssociatedGamesToPlaylist(Exception):
    pass