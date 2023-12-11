from breweries_assignment import request_call

url = "https://informed-data-challenge.netlify.app/api/breweries"

# calling a function from a different file
db_insert = request_call(url)

print(db_insert)