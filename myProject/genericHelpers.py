import requests


# EFFECTS: returns the content of an image if uri is valid, else raises error TODO:(maybe fix this or handle error)
#          this content can be packed into a Django imageFile.
def dowloadImageFromUri(uri):
    response = requests.get(uri)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception('Failed to download image')