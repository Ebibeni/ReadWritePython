import requests
import json
import pandas as pd
import csv

# Instruction
# Get the data from the API first and then save it as a CSV file or a Json file
# and then use the data from the file.

# ID to UPDATED ON FIELDS ONLY.
# Importing data via APi and assigning the request to Breweries_data
url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?"
file_path = "/Users/jamesbeni/Downloads/ReadWriteDE/ReadWritePython/data_file/output_data1.csv"
# defining the url function
def request_call(url_value):
    chicago_crime_data = requests.get(url_value)
    chicago_crime_data_json = chicago_crime_data.json()

    return chicago_crime_data_json

    


chicago_crime_data_json_value = request_call(url)
# print(chicago_crime_data_json_value)

df = pd.DataFrame(chicago_crime_data_json_value)
print(df)

df.to_csv(file_path, index=False)
# files.download('Chicago_Crime.csv')


# #Assigning the url to api_url
# api_url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?"

# # File path to the .CSV file on our local machine.
# csv_file_path = "/Users/jamesbeni/Downloads/ReadWriteDE/ReadWritePython/data_file/output_data.csv"  # Replace with your desired CSV file path

# # Function to fetch data from the API
# def fetch_data_from_api(api_url):
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         data = response.json()  # Assuming the API returns JSON data
#         return data
#     else:
#         print(f"Error fetching data from API. Status code: {response.status_code}")
#         return None

# #Function to save data from api to into excel file
# def save_data_to_csv(data, csv_file_path):
#     if data:
#         with open(csv_file_path, 'w', newline='') as csv_file:
#             csv_writer = csv.writer(csv_file)
            
#             # API response is a list of dictionaries
#             # Write the header row
#             csv_writer.writerow(data[0].keys())
            
#             # Write the data rows
#             for row in data:
#                 csv_writer.writerow(row.values())

#         print(f"Data saved to {csv_file_path}")
#     else:
#         print("No data to save.")


# # Fetch data from the API
# api_data = fetch_data_from_api(api_url)

# # Save data to CSV file
# save_data_to_csv(api_data, csv_file_path)
