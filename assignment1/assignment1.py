import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import hashlib

with open("lab3/fred_apikey.txt", "r") as f:
    apikey = f.readline().strip()

series_id = "SP500"
observation_start = "2019-01-01"
observation_end = "2024-01-01"

url = (f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={apikey}&observation_start={observation_start}&observation_end={observation_end}&file_type=json")

response = requests.get(url)
response.raise_for_status()

json_data = response.json()

with open("assignment1/data/sp500.json", 'w') as f:
    f.write(json.dumps(json_data, indent=4))

df = pd.json_normalize(json_data, 'observations')
df.drop(columns=['realtime_start', 'realtime_end'],inplace=True)
df = df[df['value'] != "."]
df['date'] = pd.to_datetime(df['date'])
df['value'] = pd.to_numeric(df['value'])
df = df.set_index(['date'])

df.to_csv("assignment1/data/sp500.csv", lineterminator='\n')

with open("assignment1/data/sp500.csv", 'rb') as f:
    data = f.read()
    hash = hashlib.sha256(data).hexdigest()

with open("assignment1/data/sp500.sha", 'w') as f:
    f.write(hash)

plt = df.plot(title="S&P 500 (2019-2024)",legend=False)
plt.set_xlabel("Date")
plt.set_ylabel("Index Value")
plt.get_figure().savefig("assignment1/results/sp500.png")