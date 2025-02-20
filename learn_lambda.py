# import os
# import json
# import spotipy
# # import boto3
# import datetime as dt


# with open("keys.json") as f:
#     keys = json.load(f)

# client_id = keys["client_id"]
# client_secret = keys["client_secret_key"]
# redirect_uri = keys["redirect_uri"]

# auth = spotipy.SpotifyOAuth(
#     client_id = client_id,
#     client_secret = client_secret,
#     redirect_uri = redirect_uri,
#     scope = "user-read-recently-played"
# )

# sp = spotipy.Spotify(auth_manager = auth)

# # def lambda_handler(events, context):
    
# tracks = sp.current_user_recently_played(limit = 10)

# if tracks is None or len(tracks['items']) == 0:
#     print({"statusCode": 404, "message": "No recent tracks found"})
# else:
#     print({"statusCode": 200, "tracks": tracks['items']})

# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extract import SpotifyClient
# import extract.FileManager.file_manager as fm

newfile = SpotifyClient()
print(newfile.get_recently_played())