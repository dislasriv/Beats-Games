import requests
import datetime

# EFFECTS: returns the content of an image if uri is valid, else raises error TODO:(maybe fix this or handle error)
#          this content can be packed into a Django imageFile.
def dowloadImageFromUri(uri):
    response = requests.get(uri)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception('Failed to download image')
    
# EFFECTS: Converts unix integer timestamp inputted into a day and time,
#          returns a datetime.datetime object that MUST BE PROCESSED AFTER.
def unixtimeToDate(unixTimeStamp):
    time = datetime.datetime.fromtimestamp(unixTimeStamp)
    return time