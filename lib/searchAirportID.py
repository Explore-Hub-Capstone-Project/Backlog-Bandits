import requests
import json
import os

api_key = os.getenv("RAPIDAPI_KEY")


def get_parent_id(query):
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchAirport"
    querystring = {"query": query}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com",
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        parent_id = data["data"][0]["details"]["parent_id"]
        airport_code = data["data"][0]["airportCode"]
        return parent_id, airport_code
    except Exception:
        return None, None


def getID():
    query = input("Enter Departing City Name: ")
    return get_parent_id(query)


def getID2():
    query = input("Enter Arrival City Name: ")
    return get_parent_id(query)


def get_airport_details():
    parent_id1, airport_code1 = getID()
    parent_id2, airport_code2 = getID2()
    return parent_id1, parent_id2, airport_code1, airport_code2


if __name__ == "__main__":
    get_airport_details()
