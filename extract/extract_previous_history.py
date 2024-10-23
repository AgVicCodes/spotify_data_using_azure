import json
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

with open("keys.json") as file:
    keys = json.load(file)

client = SpotifyOAuth(
    client_id = keys["client_id"],
    client_secret = keys["client_secret_key"],
    redirect_uri = keys["redirect_uri"],
    scope = "user-read-recently-played"
)



