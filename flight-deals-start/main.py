# Import necessary modules
import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

# Initialize NotificationManager
notification_manager = NotificationManager()

# Initialize DataManager to handle data operations
data_manager = DataManager()

# Retrieve destination data from the data manager
data_sheet = data_manager.get_destination_data()

# Print the retrieved data for inspection
pprint(data_sheet)

# Initialize FlightSearch for IATA code lookup
flight_search = FlightSearch()

# If IATA codes are missing, fetch and update them
if data_sheet[0]["iataCode"] == "":
    for city in data_sheet:
        city["iataCode"] = flight_search.Iata(city["city"])

# Print the updated data with IATA codes
pprint(data_sheet)
# Update destination codes in the data manager
data_manager.destination_data = data_sheet
data_manager.update_destination_codes()

# Search for flight data for each destination
for city in data_sheet:
    flight_search.search(city["iataCode"])

# Print the flight data for inspection
print(flight_search.flightdata.dicts)

# Update city prices if lower and send notifications
for city in data_sheet:
    curr_flight_search = flight_search.flightdata.dicts[city["city"]]

    # Check if the current lowest price is higher than the new price
    if int(city["lowestPrice"]) > int(curr_flight_search["price"]):
        # Update destination price in the data manager
        data_manager.update_destination_price(curr_flight_search["price"], city["id"])

        # Send an SMS notification with the low price alert
        notification_manager.send_sms(
            message=f"Low price alert! Only £{curr_flight_search['price']} to fly from London-{city['city']}, from {curr_flight_search['date_arrival']} to {curr_flight_search['date_departure']}."
        )
