

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
            "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
            "area": [8.516, 17.10, 3.286, 9.597, 1.221],
            "population": [200.4, 143.5, 1252, 1357, 52.98]
            }

#[Brazil,Brasilia,8.516,200.4]

keys = dict.keys()
values = dict.values()

# #Print all keys using the keys method

# for key in dict.keys():
#     print(key)
#     for value in dict.values():
#         print(value)

# empty_dict = {}
# final_list = []


# for key in dict:
#     print(key)
#     for value in dict.values():
#         print(value)



# for value in dict.values():
#      print(value)


#Print all keys and values using the items method

# for key, value in dict.items():
#      print(f"{key}: {value}")

# print(keys)

# print(values)

# First method. THE CORRECT ONE
# Get the number of countries
# num_countries = len(dict["country"])

# Loop through the dictionary and list
# for i in range(num_countries):
#     print(f"Country: {dict['country'][i]}")
#     print(f"Capital: {dict['capital'][i]}")
#     print(f"Area: {dict['area'][i]} Square Meters")
#     print(f"Population: {dict['population'][i]} Million")
#     print("\n")


# Second method. THE CORRECT ONE
# Get the number of countries
num_countries = len(dict["country"])

list_results = []

# Loop through the dictionary, list and append it to an empty List and print that List

# for i in range(num_countries):
#     list_of_countries = [
#         dict["country"][i],
#         dict["capital"][i],
#         dict["area"][i],
#         dict["population"][i]
#     ]
#     list_results.append(list_of_countries)

# print(list_results)


# Third method. THE CORRECT ONE
# Get the number of countries
num_countries = len(dict["country"])

for i in range(num_countries):
    country_list=[]

    for key, value in dict.items():
        country_list.append(value[i])
    print(country_list)


