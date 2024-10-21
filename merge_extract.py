import json
import spotipy
import pandas as pd
from extract_recent_local import sp
from glob import glob as gg

# json_files = gg(f"recently_played*.json")

# df = pd.DataFrame()

# for file in json_files:
# 	temp = pd.json_normalize(file)
# 	df = df._append(temp)

# print(df.head())

with open("recently_played1.json", "r") as file:
    data = json.load(file)

print(data["items"][19]["track"]["album"]["id"])

song_id = data["items"][19]["track"]["album"]["id"]

# try:
#     analytics = sp.audio_analysis(song_url)
# except:
#     raise Exception(f"Not working")

try:
    analysis = sp.audio_analysis(song_id)
    print(analysis)
except spotipy.exceptions.SpotifyException as e:
    print(f"Spotify API Error: {e}")
    # Fallback to audio features
    try:
        features = sp.audio_features(song_id)
        print(features)
    except Exception as fe:
        print(f"Audio features not available: {fe}")

# print(analytics)

# print(song_url)