import requests
import os
import json

# from searchFlights import push_arrival_id

# parent_id2 = push_arrival_id()

# parent_id2 = "297628"
api_key = os.getenv("RAPIDAPI_KEY")


def fetch_attractions(parent_id2):
    url = "https://tourist-attraction.p.rapidapi.com/search"

    querystring = {
        "location_id": parent_id2,
        "language": "en_US",
        "currency": "USD",
        "offset": "0",
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "tourist-attraction.p.rapidapi.com",
    }

    response = requests.post(url, data=querystring, headers=headers)
    data = response.json()

    for index, attraction in enumerate(
        data.get("results", {}).get("data", [])[:5], start=1
    ):
        name = attraction.get("name", "N/A")
        location_string = attraction.get("location_string", "N/A")
        caption = attraction.get("photo", {}).get("caption", "N/A")
        ranking_subcategory = attraction.get("ranking_subcategory", "N/A")
        rating = attraction.get("rating", "N/A")
        open_now_text = attraction.get("open_now_text", "N/A")
        neighborhood_info = ", ".join(
            [n.get("name", "N/A") for n in attraction.get("neighborhood_info", [])]
        )
        description = attraction.get("description", "N/A")
        address = attraction.get("address", "N/A")
        subtype_names = ", ".join(
            [s.get("name", "N/A") for s in attraction.get("subtype", [])]
        )

        print(
            f"Attraction {index}:\nName: {name}\nLocation: {location_string}\nCaption: {caption}\nRanking: {ranking_subcategory}\n"
            f"Rating: {rating}\nOpen Now: {open_now_text}\nNeighborhood: {neighborhood_info}\n"
            f"Description: {description}\nAddress: {address}\nSubtypes: {subtype_names}\n"
            + "--" * 35
        )
