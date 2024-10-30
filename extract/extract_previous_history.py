import json
import time
import glob
from datetime import datetime, timedelta
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

spotify = sp.Spotify(auth_manager = client)

days_to_subtract = len(glob.glob(f"data/pre-29-10/*.json"))

initial_date = int(time.mktime((datetime(2024, 9, 29) + timedelta(days = days_to_subtract)).timetuple()))

print(initial_date)

print(24/7)