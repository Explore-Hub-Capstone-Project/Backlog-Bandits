import requests
import os
import json

# from searchFlights import push_arrival_id, push_date

# parent_id2 = push_arrival_id()
# date = push_date()

api_key = os.getenv("RAPIDAPI_KEY")


def fetch_hotels(parent_id2, checkInDate, checkOutDate):
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"

    querystring = {
        "geoId": parent_id2,
        "checkIn": checkInDate,
        "checkOut": checkOutDate,
        "pageNumber": "1",
        "currencyCode": "USD",
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    hotels = data.get("data", {}).get("data", [])

    for i, hotel in enumerate(hotels[:5]):
        print(f"Hotel {i+1}:")
        print(f"Title: {hotel.get('title', 'N/A')}")
        address = f"{hotel.get('secondaryInfo', 'N/A')}"
        information = f"{hotel.get('primaryInfo', 'N/A')}"
        print(f"More Information: {information}")
        print(f"Address: {address}")
        print(f"Price: {hotel.get('priceForDisplay', 'N/A')}")
        rating = (
            hotel.get("bubbleRating", {}).get("rating", "N/A")
            if isinstance(hotel.get("bubbleRating"), dict)
            else "N/A"
        )
        print(f"Ratings: {rating}/5")
        print(
            f"Check-in: {querystring['checkIn']}, Check-out: {querystring['checkOut']}"
        )
        print("\n" + "-" * 70 + "\n")
