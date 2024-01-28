import requests
import json

# Instruction
# Get the data from the API first and then save it as a CSV file or a Json file
# and then use the data from the file.

#ID to UPDATED ON FIELDS ONLY.
# Importing data via APi and assigning the request to Breweries_data
url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?"

# defining the url function
def request_call(url_value):
    chicago_crime_data = requests.get(url_value)
    chicago_crime_data_json = chicago_crime_data.json()

    return chicago_crime_data_json

def data_manipulation(chicago_crime_data_json_value):
    length_chicago_crime_data = len(chicago_crime_data_json_value)
    new_chicago_crime_data = {}

    for index in range(length_chicago_crime_data):

        # print(index)
        for key in chicago_crime_data_json_value[index]:
            # print(chicago_crime_data_json_value[index][key])
            print(key)


    

    


chicago_crime_data_json_value = request_call(url)
# print(data_manipulation(chicago_crime_data_json_value))
# data_manipulation(chicago_crime_data_json_value)
print(data_manipulation(chicago_crime_data_json_value))