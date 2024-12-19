#Script to fetch data from APIs

import pandas as pd
import requests

API_URL = "https://api.rise-brand.com/live_campaign_data"

def fetch_live_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv("data/live_data.csv", index=False)
        print("Live data fetched and saved to data/live_data.csv")
    else:
        print(f"Failed to fetch live data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_live_data()