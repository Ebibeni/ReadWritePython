

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


# Get the number of countries
num_countries = len(dict["country"])

# Loop through the dictionary and list
for i in range(num_countries):
    print(f"Country: {dict['country'][i]}")
    print(f"Capital: {dict['capital'][i]}")
    print(f"Area: {dict['area'][i]} million square km")
    print(f"Population: {dict['population'][i]} million")
    print("\n")