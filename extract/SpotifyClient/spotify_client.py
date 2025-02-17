import os
import sys
import json
import time
import spotipy
from spotipy import SpotifyOAuth
from FileManager.file_manager import FileManager
# from spotipy.oauth2 import SpotifyOAuth

class SpotifyClient:
    def __init__(self, scope = "user-read-recently-played"):
        self.keys = self.load_keys()
        self.auth_manager = SpotifyOAuth(
            client_id = self.keys["client_id"],
            client_secret = self.keys["client_secret_key"],
            redirect_uri = self.keys["redirect_uri"],
            scope = scope
        )
        self.sp = spotipy.Spotify(auth_manager = self.auth_manager)
        self.file_manager = FileManager()

    def load_keys(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        path = os.path.join(base_dir, "keys.json")
        with open(path, "r") as file:
            keys = json.load(file)
        return keys
    
    def get_recently_played(self, ):
        current_time = int(time.time())
        recent_playback = self.sp.current_user_recently_played(limit = 50, before = current_time)
        self.file_manager.save_file(recent_playback)

client = SpotifyClient()
client.get_recently_played()