# import json
# import time
# import glob
# from datetime import datetime, timedelta
# import spotipy as sp
# from spotipy.oauth2 import SpotifyOAuth

# with open("keys.json") as file:
#     keys = json.load(file)

# client = SpotifyOAuth(
#     client_id = keys["CLIENT_ID"],
#     client_secret = keys["CLIENT_SECRET_KEY"],
#     redirect_uri = keys["REDIRECT_URI"],
#     scope = "user-read-recently-played"
# )

# spotify = sp.Spotify(auth_manager = client)

# days_to_subtract = len(glob.glob(f"data/pre-29-10/*.json"))

# initial_date = int(time.mktime((datetime(2024, 9, 29) - timedelta(days = days_to_subtract)).timetuple()))

# history = spotify.current_user_recently_played(limit = 50, before = int(time.time() - 1 * 86400))

# with open(f"data/pre-29-10/recently_played{days_to_subtract}.json", "w") as file:
#     json.dump(history, file, indent = 4)

access_token = "BQAKLdHVyynFpSbgFYcxQcfszFbOJhJfxsCrSLrqYc_NmDwTuaMxtkyLbUF7Fd8RcXuOJhAgcx1dYUL8PuhVXLk8Oc_U_vhxYOTaOdQlryTNwr99_xsqWiqSbD2NfOD8kG8TYA-kfQs8hpd6-CA64rX5rGc7MNndbk_Sc4ZqI34fU1ublRGxDl3U8iPfSLYXy0LjiUGsf57IVIQ8pZrqdxo8Zg"

import requests

# Replace this with your actual OAuth token
# access_token = "YOUR_SPOTIFY_ACCESS_TOKEN"

# The endpoint URL
url = "https://api.spotify.com/v1/me/player/recently-played?before=1730230320&limit=50"

# Set up headers with the access token
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Make the request
response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    history = response.json()
    print(history)
else:
    print(f"Error: {response.status_code}", response.text)

# curl -X GET "https://api.spotify.com/v1/me/player/recently-played?limit=50" -H "Authorization: Bearer BQAKLdHVyynFpSbgFYcxQcfszFbOJhJfxsCrSLrqYc_NmDwTuaMxtkyLbUF7Fd8RcXuOJhAgcx1dYUL8PuhVXLk8Oc_U_vhxYOTaOdQlryTNwr99_xsqWiqSbD2NfOD8kG8TYA-kfQs8hpd6-CA64rX5rGc7MNndbk_Sc4ZqI34fU1ublRGxDl3U8iPfSLYXy0LjiUGsf57IVIQ8pZrqdxo8Zg"

# curl -X GET "https://api.spotify.com/v1/me/player/recently-played?limit=50" -H "Authorization: Bearer BQAEPiiJc4F4gK-DQDt3ANp_3-K6OJK6bfQHh1IQXKDuH24DGMNiXQjgnSKfEMWtkesN9YmKB6WZ9wy2D1pCt0MsN93CAPTRssSTdXNj9X8kokwOZ1AfD8oshAUlrvt1lzm2psDN2VQSVa-l0-vO4TuVGzjvdn1qp441mmeoifjojeQ2wvL6RD6nnGT1-e1ZxZAZMmqy9-BbToYs36mnOELSHA"