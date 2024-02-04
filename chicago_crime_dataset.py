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


# case_id= [dictionary["id"] for dictionary in api_data]
# case_number= [dictionary["case_number"] for dictionary in api_data]

# print(case_id)
# print(case_number)
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
        

df = pd.DataFrame(api_data)
# # print(df)
# for i in df:
#     for key, value in df.items():
#         print(key,value)

# df.to_csv(file_path, index=False)
