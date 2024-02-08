import requests
from datetime import datetime
import os

api_key = os.getenv("RAPIDAPI_KEY")

from searchAirportID import get_airport_details

parent_id1, parent_id2, airport_code1, airport_code2 = get_airport_details()

print(f"Departing City ID: {parent_id1}, Departing City Code: {airport_code1}")
print(f"Arriving City ID: {parent_id2}, Arriving City Code: {airport_code2}")


date = input("Enter Date (YYYY-MM-DD) : ")
# itinerary_type = input("Enter Itinerary Type (ONE_WAY / ROUND_TRIP) : ")
itinerary_type = "ONE_WAY"
sort_order = input("Enter Sort Order (PRICE / DURATION) : ")
number_of_adults = input("Enter Number of Adults : ")
# number_of_seniors = input("Enter Number of Seniors : ")
number_of_seniors = 0
class_of_service = input("Enter Class (ECONOMY / PREMIUM_ECONOMY): ")
# number_of_pages = input("Enter Page Number (1) : ")
number_of_pages = 1
currency_code = input("Enter Currency Code : ")

print("-" * 70)


def convert_time(time_str):
    return datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z").strftime(
        "%d %b %Y %H:%M %Z"
    )


def fetch_flight_details(
    airport_code1,
    airport_code2,
    date,
    itinerary_type,
    sort_order,
    number_of_adults,
    number_of_seniors,
    class_of_service,
    number_of_pages,
    currency_code,
):
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"
    querystring = {
        "sourceAirportCode": airport_code1,
        "destinationAirportCode": airport_code2,
        "date": date,
        "itineraryType": itinerary_type,
        "sortOrder": sort_order,
        "numAdults": number_of_adults,
        "numSeniors": number_of_seniors,
        "classOfService": class_of_service,
        "pageNumber": number_of_pages,
        "currencyCode": currency_code,
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    flights = response.json().get("data", {}).get("flights", [])

    for idx, flight in enumerate(flights[:5], start=1):
        print(f"Flight {idx}:")
        if flight["segments"]:
            segment = flight["segments"][0]
            if segment["legs"]:
                leg = segment["legs"][0]
                departure_time = datetime.strptime(
                    leg["departureDateTime"], "%Y-%m-%dT%H:%M:%S%z"
                ).strftime("%Y-%m-%d %H:%M")
                arrival_time = datetime.strptime(
                    leg["arrivalDateTime"], "%Y-%m-%dT%H:%M:%S%z"
                ).strftime("%Y-%m-%d %H:%M")
                print(f"Airline Name: {leg['operatingCarrier']['displayName']}")
                print(f"Flight Number: {leg['flightNumber']}")
                print(f"Origin: {leg['originStationCode']}")
                print(f"Destination: {leg['destinationStationCode']}")
                print(f"Departure -> Arrival: {departure_time} -> {arrival_time}")
                print(f"Class of Service: {leg['classOfService']}")
                number_of_stops = (
                    "Direct" if leg["numStops"] == 0 else f"{leg['numStops']} Stop(s)"
                )
                print(f"Number of Stops: {number_of_stops}")
                print(f"Price of Flight: {flight['purchaseLinks'][0]['totalPrice']}")
                print("\n" + "-" * 70 + "\n")


fetch_flight_details(
    airport_code1,
    airport_code2,
    date,
    itinerary_type,
    sort_order,
    number_of_adults,
    number_of_seniors,
    class_of_service,
    number_of_pages,
    currency_code,
)


def push_arrival_id():
    return parent_id2, date
