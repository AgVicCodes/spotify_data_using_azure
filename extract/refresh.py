import os
import requests

def refresh_access_token():
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    refresh_token = os.getenv('REFRESH_TOKEN')
    url = "https://accounts.spotify.com/api/token"
    
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    headers = {
        "Authorization": f"Basic {client_id}:{client_secret}".encode('ascii').decode('ascii')
    }

    response = requests.post(url, data = payload, headers = headers)
    return response.json().get("access_token")