
# https://informed-data-challenge.netlify.app/api/breweries
# name, street, city, state, country, phone number and website.

# Breweries_data = {
#     "data": [
#     {
#     "id": "10-56-brewing-company-knox",
#     "name": "10-56 Brewing Company",
#     "brewery_type": "micro",
#     "street": "400 Brown Cir",
#     "address_2": "",
#     "address_3": "",
#     "city": "Knox",
#     "state": "Indiana",
#     "county_province": "",
#     "postal_code": "46534",
#     "website_url": "",
#     "phone": "6308165790",
#     "country": "United States",
#     "longitude": "-86.627954",
#     "latitude": "41.289715",
#     "tags": "",
#     "rating": "4.859999999999999",
#     "number_of_ratings": "46070"
#     },
#     {
#     "id": "10-barrel-brewing-co-bend-1",
#     "name": "10 Barrel Brewing Co",
#     "brewery_type": "large",
#     "street": "62970 18th St",
#     "address_2": "",
#     "address_3": "",
#     "city": "Bend",
#     "state": "Oregon",
#     "county_province": "",
#     "postal_code": "97701-9847",
#     "website_url": "http://www.10barrel.com",
#     "phone": "5415851007",
#     "country": "United States",
#     "longitude": "-121.28170597038259",
#     "latitude": "44.08683530625218",
#     "tags": "",
#     "rating": "4.24",
#     "number_of_ratings": "93220"
#     },
#     {
#     "id": "10-barrel-brewing-co-bend-2",
#     "name": "10 Barrel Brewing Co",
#     "brewery_type": "large",
#     "street": "1135 NW Galveston Ave Ste B",
#     "address_2": "",
#     "address_3": "",
#     "city": "Bend",
#     "state": "Oregon",
#     "county_province": "",
#     "postal_code": "97703-2465",
#     "website_url": "",
#     "phone": "5415851007",
#     "country": "United States",
#     "longitude": "-121.32880209261799",
#     "latitude": "44.057564901366796",
#     "tags": "",
#     "rating": "2.35",
#     "number_of_ratings": "97624"
#     }
#     ]
# }


import requests
import json
import pandas as pd

#Importing data via APi and assigning the request to Breweries_data
url = "https://informed-data-challenge.netlify.app/api/breweries"

# Calling url function
def request_call(url_value):
    Breweries_data = requests.get(url_value)
    breweries_json = Breweries_data.json()

    return breweries_json

#loop function to manipulate data from request_call function
def data_manipulation(breweries_json_value):

    num_Breweries_data = len(breweries_json_value["data"])
    New_Breweries_data_list = []
    # Using a for loop to loop over the vlaues of num_Breweries_data dictionary and storing them in a new dictionary called New_Breweries_data.  
    for i in range(num_Breweries_data):
        New_Breweries_data={}
        New_Breweries_data_Dynamic_Dict = {}
    # name, street, city, state, country, phone number and website.
        for key, value in breweries_json.items():
            # print(value)
            New_Breweries_data.update(value[i])
    # Using an if statement nested inside a for loop to loop over the key and vlaues of New_Breweries_data dictionary.   
        for key, value in New_Breweries_data.items():
            # print(key)
            
            if key == "name":
                # print(f"{key}: {value}")
                New_Breweries_data_Dynamic_Dict.update({key:value})
            elif key == "street":
                # print(f"{key}: {value}")
                New_Breweries_data_Dynamic_Dict.update({key:value})
            elif key == "city":
                # print(f"{key}: {value}")
                New_Breweries_data_Dynamic_Dict.update({key:value})
            elif key == "state":
                # print(f"{key}: {value}")
                New_Breweries_data_Dynamic_Dict.update({key:value})
            elif key == "country":
                # print(f"{key}: {value}")
                New_Breweries_data_Dynamic_Dict.update({key:value})
            elif key == "phone":
                # print(f"{key}: {value}")
                New_Breweries_data_Dynamic_Dict.update({key:value})
            elif key == "website_url":
                # print(f"{key}: {value}")
                New_Breweries_data_Dynamic_Dict.update({key:value})

        New_Breweries_data_list.append(New_Breweries_data_Dynamic_Dict)
        # print(New_Breweries_data)
        # print("\n")
    return New_Breweries_data_list

#created a funtion to run the pandas data frame manipulation
def pandas_data_frame(New_Breweries_data_list_value):
    
    df = pd.DataFrame(New_Breweries_data_list_value)  
    return print(df)


# calling the request function and assigning it to breweries_json
breweries_json = request_call(url)
# print(breweries_json)

# calling the data_manipulation function and assigning it to results while passing breweries_json as the arg
results = data_manipulation(breweries_json)
# print(results)

#calling the pandas data frame manipulation funtion
pandas_data_frame(results)