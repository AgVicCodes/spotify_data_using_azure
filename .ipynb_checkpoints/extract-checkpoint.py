import json
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

recently_played = sp.current_user_recently_played(limit = 50, after = "1727391600")

with open("recently_played2.json", "w") as file:
    json.dump(recently_played, file, indent = 4)