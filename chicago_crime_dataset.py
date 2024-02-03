import requests
import json
import pandas as pd
import csv
from datetime import datetime

# Instruction
# Get the data from the API first and then save it as a CSV file or a Json file
# and then use the data from the file.

#Assigning the url to api_url
api_url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?"

now = datetime.now()
Current_time = now.strftime("%H:%M:%S")
Current_time_str = str(Current_time)

file_path = "/Users/jamesbeni/Downloads/ReadWriteDE/ReadWritePython/data_file/output_data" + Current_time_str + ".csv"


# Function to fetch data from the API
def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns JSON data
        return data
    else:
        print(f"Error fetching data from API. Status code: {response.status_code}")
        return None


# Fetch data from the API
api_data = fetch_data_from_api(api_url)


df = pd.DataFrame(api_data)
print(df)

df.to_csv(file_path, index=False)
