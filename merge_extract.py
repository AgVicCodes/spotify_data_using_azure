from glob import glob as gg
import pandas as pd

json_files = gg(f"recently_played*.json")

df = pd.DataFrame()

for file in json_files:
	temp = pd.json_normalize(file)
	df = df._append(temp)

print(df.head())
