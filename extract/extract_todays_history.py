import json
import time
import glob
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

try:
    with open("keys.json") as file:
        key = json.load(file)
except FileNotFoundError as fnfe:
    raise Exception(f"File wasn't found: {fnfe}")

# client_id = os.getenv("CLIENT_ID")
# client_secret = os.getenv("CLIENT_SECRET_KEY")
# redirect_uri = os.getenv("REDIRECT_URI")

try:
    client_id = key["CLIENT_ID"]
    client_secret = key["CLIENT_SECRET_KEY"]
    redirect_uri = key["REDIRECT_URI"]
except KeyError as ke:
    raise Exception(f"Key {ke} not found")
    

print(f"Client ID: {client_id[:3]}***, Type: {type(client_id)}")
print(f"Client Secret: {client_secret[:3]}***, Type: {type(client_secret)}")
print(f"Redirect URI: {redirect_uri[:3]}***, Type: {type(redirect_uri)}")

client = SpotifyOAuth(
    client_id,
    client_secret,
    redirect_uri,
    scope = "user-read-recently-played",
    # cache_path = None
)

if not client_id or not client_secret or not redirect_uri:
    raise ValueError("Missing required environment variables")

sp = spotipy.Spotify(auth_manager = client)

json_files = glob.glob(f"data/recently_played*.json")

count = len(json_files) + 1

current_time = int(time.time())

def get_recently_played():    

    recently_played = sp.current_user_recently_played(limit = 50, after = current_time)

    with open(f"data/recently_played{count}.json", "w") as file:
        json.dump(recently_played, file, indent = 4)



get_recently_played()

# Extract playlist items
# playlist_items


# Get the current time in Unix time