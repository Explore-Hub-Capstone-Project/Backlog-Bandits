from searchFlights import fetch_flight_details
from searchHotels import fetch_hotels
from searchAttractions import fetch_attractions

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

checkOutDate = input("Enter Checkout Date for Hotel: ")
print("-" * 70)

fetch_hotels(parent_id2, date, checkOutDate)

fetch_attractions(parent_id2)
