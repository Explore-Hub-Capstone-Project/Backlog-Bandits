import requests
import json

url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"

destination1 = input("Enter Destination 1 : ")
destination2 = input("Enter Destination 2 : ")
date = input("Enter Date (YYYY-MM-DD) : ")
itineraryType = input("Enter Itinerary Type (ONE_WAY / ROUND_TRIP) : ")
sortOrder = input("Enter Sort Order (PRICE / DURATION) : ")
numAdults = input("Enter Number of Adults : ")
numSeniors = input("Enter Number of Seniors : ")
# cabin = input("Enter Cabin Code (0 for Economy) : ")
classOfService = input("Enter Class (ECONOMY / PREMIUM_ECONOMY): ")
pageNumber = input("Enter Page Number (1) : ")
currencyCode = input("Enter Currency Code : ")

querystring = {
    "sourceAirportCode": destination1,
    "destinationAirportCode": destination2,
    "date": date,
    "itineraryType": itineraryType,
    "sortOrder": sortOrder,
    "numAdults": numAdults,
    "numSeniors": numSeniors,
    "classOfService": classOfService,
    "pageNumber": pageNumber,
    "currencyCode": currencyCode,
}

headers = {
    "X-RapidAPI-Key": "22e66d4f58msh0942688c9a3a6bbp103f7ejsn284b71172003",
    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com",
}


response = requests.get(url, headers=headers, params=querystring)


json_data = response.json()
print(json_data)

with open("data.json", "w") as outfile:
    json.dump(json_data, outfile, indent=4)
