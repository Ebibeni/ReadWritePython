import requests
import json
import pandas as pd
import csv
from datetime import datetime
import mysql.connector

# Instruction
# Get the data from the API first and then save it as a CSV file or a Json file
# and then use the data from the file.

# Creating connection object and selecting Breweries DATABASE
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database="chicago_city_crime"
)

#Assigning the url to api_url
api_url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?"

# Using the date time function to get the current time on the local machine
now = datetime.now()
Current_time = now.strftime("%H:%M:%S")
Current_time_str = str(Current_time)

# Adding the current time to the file name
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

len_api_data = len(api_data)
# print(len_api_data)

def data_manipulation(api_data):
    data_List = []
    for length in api_data:
        data_dic = {}
        for key, value in length.items():
            print(key,value)
            if key == "id":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "case_number":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "date":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "block":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "iucr":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "primary_type":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "description":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "location_description":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "arrest":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "domestic":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "beat":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "district":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "ward":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "community_area":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "fbi_code":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "x_coordinate":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "y_coordinate":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "year":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "updated_on":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "latitude":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
            elif key == "longitude":
                    # print(f"{key}: {value}")
                data_dic.update({key:value})
        data_List.append(data_dic)
    return data_List

df = pd.DataFrame(api_data)
# # print(df)

# df.to_csv(file_path, index=False)

selected_data = data_manipulation(api_data)
# print(pd.DataFrame(selected_data))

#Create a DATABASE 
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE chicago_city_crime")

# id, case_number, date, block, iucr, primary_type, description, location_description, arrest, domestic, beat, district, ward, community_area, fbi_code, x_coordinate, y_coordinate, year, updated_on, latitude and longitude.

mycursor.execute("CREATE TABLE chicago_city_crime_data (id VARCHAR(255), case_number VARCHAR(255), date VARCHAR(255), block VARCHAR(255),iucr VARCHAR(255), primary_type VARCHAR(255), description VARCHAR(255), location_description VARCHAR(255), arrest VARCHAR(255), domestic VARCHAR(255), beat VARCHAR(255), district VARCHAR(255), ward VARCHAR(255), community_area VARCHAR(255), fbi_code VARCHAR(255), x_coordinate VARCHAR(255), y_coordinate VARCHAR(255),  year VARCHAR(255), updated_on VARCHAR(255), latitude VARCHAR(255), longitude VARCHAR(255))")