# https://informed-data-challenge.netlify.app/api/breweries
# name, street, city, state, country, phone number and website.

import requests
import json
import pandas as pd
import mysql.connector

# Importing data via APi and assigning the request to Breweries_data
url = "https://informed-data-challenge.netlify.app/api/breweries"

# Creating connection object and selecting Breweries DATABASE
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database="Breweries"
)

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

# print(mydb)


#Create a DATABASE 
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE breweries")

# name, street, city, state, country, phone number and website.

# mycursor.execute("CREATE TABLE breweries_data (name VARCHAR(255), street VARCHAR(255), city VARCHAR(255), state VARCHAR(255),country VARCHAR(255), phone INT, website VARCHAR(255))")

for mydict in results:
    placeholders = ', '.join(['%s'] * len(results))
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('breweries_data', columns, values)
    print(sql)

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


#Show DATABASES created
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)