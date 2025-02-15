import json
import time
import glob
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class FileManager:
    def __init__(self, directory = "data", filename_prefix = "recently_played"):
        self.directory = directory
        self.filename_prefix = filename_prefix

    def get_next_filename(self):
        json_files = glob.glob(f"{self.directory}/{self.filename_prefix}*.json")
        count = len(json_files) + 1
        return f"{self.directory}/{self.filename_prefix}{count}.json"

    def save_data(self, data):
        filename = self.get_next_filename()
        with open(filename, "w") as file:
            json.dump(data, file, indent = 4)
        print(f"Data saved to {filename}")


class SpotifyClient:
    def __init__(self, keys_path = "keys.json", scope = "user-read-recently-played"):
        self.keys = self.load_keys(keys_path)
        self.auth_manager = SpotifyOAuth(
            client_id = self.keys["client_id"],
            client_secret = self.keys["client_secret_key"],
            redirect_uri = self.keys["redirect_uri"],
            scope = scope
        )
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
        self.file_manager = FileManager()

    def load_keys(self, path):
        try:
            with open(path) as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {path} not found")
            raise

    def get_recently_played(self):
        # Get the current time (could also be abstracted if needed)
        current_time = int(time.time())
        recently_played = self.sp.current_user_recently_played(limit = 50, after = current_time)
        self.file_manager.save_data(recently_played)
        return recently_played

# Usage
if __name__ == "__main__":
    client = SpotifyClient()
    client.get_recently_played()
