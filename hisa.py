import requests
import json
import pandas as pd  # Step 1: Import Pandas library

response_API = requests.get('https://informed-data-challenge.netlify.app/api/breweries')
data = response_API.text  
parse = json.loads(data)
breweries_list = []  

for i in parse['data']:
    brewery_dict = {
        'Name': i['name'],
        'Street': i['street'],
        'City': i['city'],
        'State': i['state'],
        'Country': i['country'],
        'Phone': i['phone'],
        'Website': i['website_url']
    }
    breweries_list.append(brewery_dict) 

df = pd.DataFrame(breweries_list)  
print(df)