import json
import pandas as pd


with open("recently_played7.json", "r") as file:
    data = json.load(file)


colummn_label = [
    "album_name", 
    "album_release_date", 
    "album_uri", 
    "artist_name", 
    "track_duration", 
    "track_id", 
    "track_name"
    "track_popularity", 
    "time_played"
]

song_df = pd.DataFrame(columns = colummn_label)


df_dict = {
    "album_name": [item["track"]["album"]["name"] for item in data["items"]],
    "album_release_date": [item["track"]["album"]["release_date"] for item in data["items"]],
    "album_uri": [item["track"]["album"]["uri"] for item in data["items"]],
    "artist_name": [item["track"]["artists"][0]["name"] for item in data["items"]],
    "track_duration": [item["track"]["duration_ms"] for item in data["items"]],
    "id": [item["track"]["id"] for item in data["items"]], 
    "track_name": [item["track"]["name"] for item in data["items"]],
    "track_popularity": [item["track"]["popularity"] for item in data["items"]],
    "time_played": [item["played_at"] for item in data["items"]]
}

song_df = pd.DataFrame(df_dict)

# for item in data["items"]:

pd.set_option("display.max_columns", None)

print(song_df.head(10))


# print(item["track"]["album"]["name"])
# print(item["track"]["album"]["release_date"])
# print(item["track"]["album"]["uri"])
# print(item["track"]["artists"][0]["name"])
# print(item["track"]["duration_ms"])
# print(item["track"]["popularity"])
# print(item["played_at"])
# print("\n\n")
# df = 

# data = [
#     data["items"][i]["track"]["album"]["name"],
#     data["items"][i]["track"]["album"]["release_date"],
#     data["items"][i]["track"]["album"]["uri"],
#     data["items"][i]["track"]["artists"][0]["name"],
#     data["items"][i]["track"]["duration_ms"],
#     data["items"][i]["track"]["id"],
#     data["items"][i]["track"]["name"],
#     data["items"][i]["track"]["popularity"],
#     data["items"][i]["played_at"],
# ]