import json
import time
import glob
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


client_id = os.getenv("CLIENT_ID")[0]
client_secret = os.getenv("CLIENT_SECRET_KEY")[0]
redirect_uri = os.getenv("REDIRECT_URI")[0]

print(f"Client ID: {client_id}, Type: {type(client_id)}")
print(f"Client Secret: {client_secret}, Type: {type(client_secret)}")
print(f"Redirect URI: {redirect_uri}, Type: {type(redirect_uri)}")

client = SpotifyOAuth(
    client_id,
    client_secret,
    redirect_uri,
    scope = "user-read-recently-played"
)

if not client_id or not client_secret or not redirect_uri:
    raise ValueError("Missing required environment variables")

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