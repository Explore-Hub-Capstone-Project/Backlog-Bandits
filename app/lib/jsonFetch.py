import json

with open("data.json", "r") as file:
    data = json.load(file)

flights = data["data"]["flights"]

for flight in flights:
    for segment in flight["segments"]:
        for leg in segment["legs"]:
            print(f"Flight Number: {leg['flightNumber']}")
            print(
                f"Origin: {leg['originStationCode']} -> Destination: {leg['destinationStationCode']}"
            )
            print(f"Number of Stops: {leg['numStops']}")
            print(
                f"Departure: {leg['departureDateTime']} -> Arrival: {leg['arrivalDateTime']}"
            )
            print(
                f"Carrier: {leg['marketingCarrierCode']}, Aircraft: {leg['equipmentId']}"
            )
            print(f"Class of Service: {leg['classOfService']}")
            print("-" * 60)
