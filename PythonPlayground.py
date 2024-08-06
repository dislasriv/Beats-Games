import requests

def main():
    busa = requests.get("https://api.spotify.com/v1/playlists/20g1GYEqzeiD8IMpSMj21J")
    print("CHESTO")
    print(busa)

if __name__ == "__main__":
    main()

