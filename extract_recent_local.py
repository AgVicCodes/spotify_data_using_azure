import json
import time
import glob
import spotipy
from spotipy.oauth2 import SpotifyOAuth

with open("keys.json") as file:
    keys = json.load(file)

client = SpotifyOAuth(
    client_id = keys["client_id"], 
    client_secret = keys["client_secret_key"], 
    redirect_uri = keys["redirect_uri"], 
    scope = "user-read-recently-played"
)

sp = spotipy.Spotify(auth_manager = client)

json_files = glob.glob(f"recently_played*.json")

count = len(json_files) + 1

current_time = int(time.time())

def get_recently_played():    

    recently_played = sp.current_user_recently_played(limit = 50, after = current_time)

    with open(f"recently_played{count}.json", "w") as file:
        json.dump(recently_played, file, indent = 4)



get_recently_played()

# Extract playlist items
# playlist_items


# Get the current time in Unix time