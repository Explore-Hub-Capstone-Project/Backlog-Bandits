import requests
from datetime import datetime
import os

api_key = os.getenv("RAPIDAPI_KEY")

from searchAirportID import get_airport_details

parent_id1, parent_id2, airport_code1, airport_code2 = get_airport_details()

print(f"Departing City ID: {parent_id1}, Departing City Code: {airport_code1}")
print(f"Arriving City ID: {parent_id2}, Arriving City Code: {airport_code2}")


date = input("Enter Date (YYYY-MM-DD) : ")
itinerary_type = input("Enter Itinerary Type (ONE_WAY / ROUND_TRIP) : ")
sort_order = input("Enter Sort Order (PRICE / DURATION) : ")
number_of_adults = input("Enter Number of Adults : ")
number_of_seniors = input("Enter Number of Seniors : ")
class_of_service = input("Enter Class (ECONOMY / PREMIUM_ECONOMY): ")
number_of_pages = input("Enter Page Number (1) : ")
currency_code = input("Enter Currency Code : ")


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
        "X-RapidAPI-Key": "RAPDIAPI_KEY",
        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    flights = response.json().get("data", {}).get("flights", [])

    for idx, flight in enumerate(flights[:5], start=1):
        for segment in flight["segments"]:
            for leg in segment["legs"]:
                departure_time = datetime.strptime(
                    leg["departureDateTime"], "%Y-%m-%dT%H:%M:%S%z"
                ).strftime("%Y-%m-%d %H:%M")
                arrival_time = datetime.strptime(
                    leg["arrivalDateTime"], "%Y-%m-%dT%H:%M:%S%z"
                ).strftime("%Y-%m-%d %H:%M")
                flight_details = {
                    "S/N": idx,
                    "Airline Name": leg["operatingCarrier"]["displayName"],
                    "Airline Number": leg["flightNumber"],
                    "Origin": leg["originStationCode"],
                    "Destination": leg["destinationStationCode"],
                    "Time of Flight": f"{departure_time} -> {arrival_time}",
                    "Class of Flight": leg["classOfService"],
                    "Number of Stops": (
                        "Direct"
                        if leg["numStops"] == 0
                        else f"{leg['numStops']} Stop(s)"
                    ),
                    "Stops Location": "N/A",
                    # "Logo URL": leg["operatingCarrier"]["logoUrl"],
                    "Price of Flight": flight["purchaseLinks"][0]["totalPrice"],
                    # "Purchase Link": flight["purchaseLinks"][0]["url"],
                }
                # print(idx, ":")
                print(flight_details)
                print(
                    "-------------------------------------------------------------------"
                )


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
    return parent_id2
