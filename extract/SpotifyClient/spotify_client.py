import os
import json
import time
import logging
import spotipy
import requests
from spotipy import SpotifyOAuth
from extract.FileManager.file_manager import FileManager

class SpotifyClient:
    """
    A client to interact with the Spotify API for retrieving recently played tracks.
    This class handles authentication with Spotify using OAuth and fetches recent playback data.

    """
    def __init__(self, env = "local", scope = "user-read-recently-played"):
        """
        Initializes the SpotifyClient with authentication credentials.

        :param scope: Scope of access for Spotify API (default is "user-read-recently-played").
        
        """
        logging.info("Initialising SpotifyCLient...")

        self.keys = self.load_keys()
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.redirect_uri = os.getenv('REDIRECT_URI')
        self.refresh_token = os.getenv('REFRESH_TOKEN')
        

        if env == "local":
            self.auth_manager = SpotifyOAuth(
                client_id = self.keys["client_id"],
                client_secret_key = self.keys["client_secret_key"],
                redirect_uri = self.keys["redirect_uri"],
                scope = scope
            )

        elif env == "cloud":
            self.auth_manager = SpotifyOAuth(
                client_id = self.client_id,
                client_secret = self.client_secret,
                redirect_uri = self.redirect_uri,
                scope = scope
            )
            
        else:
            logging.warning("Environment not set. Please set environment to either local or cloud!")

        self.sp = spotipy.Spotify(auth_manager = self.auth_manager)
        self.file_manager = FileManager()

        logging.info(f"SpotifyClient successfully initialised with scope {scope}")

    def load_keys(self):
        """
        Loads Spotify API credentials from the `keys.json` file.
        :raise FileNotFoundError: If `keys.json` is not found in the project root directory.
        :return keys: A dictionary containing client details
        """
        try:
            logging.info(f"Loading API Keys...")

            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            path = os.path.join(base_dir, "keys.json")
            with open(path, "r") as file:
                keys = json.load(file)
            
            logging.info(f"API Keys successfully retrieved!")

            return keys
        except FileNotFoundError:
            logging.error(f"File {path} not found! Please make API credentials are correctly set!")
    
    def get_recently_played(self):
        """
        Fetches recently played tracks from Spotify API and saves them as a JSON file.

        The fetched data includes details of the last 50 tracks played before the current timestamp.

        The data is saved using the `FileManager.save_file()` method.

        :raises spotipy.exceptions.SpotifyException: If there is an issue with the API request.
        
        """
        try:
            logging.info("Fetching recently played tracks from Spotify...")
            current_time = int(time.time())
            recent_playback = self.sp.current_user_recently_played(limit = 50, after = current_time)

            logging.info(f"Playback history successfully extracted!")

            self.file_manager.save_file(recent_playback)
        except spotipy.exceptions.SpotifyException as se:
            logging.error(f"Error getting playback history: {se}")
            raise Exception(f"Exception: {se}")
        
    def refresh_access_token(self):
        """
        Refreshes the Spotify access token using the refresh token.

        This method sends a POST request to the Spotify API to obtain a new access token.
        It uses the stored refresh token to authenticate the request.

        :return: The new access token as a string, or None if the request fails.
        :rtype: str
        """
        try:
            logging.info("Refreshing Spotify access token...")
            url = "https://accounts.spotify.com/api/token"
            
            payload = {
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token
            }
            headers = {
                "Authorization": f"Basic {self.client_id}:{self.client_secret}".encode('ascii').decode('ascii')
            }
            response = requests.post(url, data = payload, headers = headers)
            access_token = response.json().get("access_token")

            if access_token:
                logging.info(f"Access token successfully refreshed!")
            else:
                logging.warning(f"Failed to refresh access token.")
            
            return access_token
        
        except Exception as e:
            logging.error(f"Error refreshing access token: {e}")
            return None
