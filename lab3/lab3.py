import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import hashlib

with open("lab3/fred_apikey.txt", "r") as f:
    apikey = f.readline().strip()

series_id = "DJIA"
observation_start = "2019-01-01"
observation_end = "2023-01-01"

url = (f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={apikey}&observation_start={observation_start}&observation_end={observation_end}&file_type=json")

response = requests.get(url)
response.raise_for_status()

json_data = response.json()

with open("lab3/djia.json", "w") as f:
    f.write(json.dumps(json_data, indent=4))

df = pd.json_normalize(json_data, 'observations')

df.drop(columns=['realtime_start', 'realtime_end'],inplace=True)

df = df[df['value'] != "."]

df['date'] = pd.to_datetime(df['date'])
df['value'] = pd.to_numeric(df['value'])

df = df.set_index(['date'])

df.to_csv("lab3/djia.csv")

print(df.head())
print(df.dtypes)

plt = df.plot(title="DJIA (2019-2023)",legend=False)
plt.set_xlabel("Date")
plt.set_ylabel("Index Value")
plt.get_figure().savefig("lab3/djia.png")

with open("lab3/djia.csv", "rb") as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

with open("lab3/djia.sha", 'w') as f:
    f.write(sha256hash)