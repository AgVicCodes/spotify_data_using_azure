import json
import spotipy
import pandas as pd
from extract_recent import sp
from glob import glob as gg

# json_files = gg(f"recently_played*.json")

# df = pd.DataFrame()

# for file in json_files:
# 	temp = pd.json_normalize(file)
# 	df = df._append(temp)

# print(df.head())

with open("recently_played1.json", "r") as file:
    data = json.load(file)

print(data["items"][0]["track"]["album"]["id"])

song_url = data["items"][0]["track"]["album"]["id"]

analytics = sp.audio_analysis(song_url)

print(analytics)