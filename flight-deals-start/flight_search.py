KIWI_END_POINT = "https://api.tequila.kiwi.com"
import requests
import os
from datetime import timedelta, date, timezone, datetime
from flight_data import FlightData

# Get the Kiwi API key from the environment variable
kiwi_key = os.environ.get("KIWI_KEY")

class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    It provides methods to get IATA codes for cities and perform flight searches.
    """

    def __init__(self):
        """
        Initializes a new instance of the FlightSearch class.
        """
        # Initialize an instance of the FlightData class to store flight information
        self.flightdata = FlightData()

    def Iata(self, city_name):
        """
        Gets the IATA code for a given city.

        :param city_name: The name of the city for which to get the IATA code.
        :return: The IATA code for the specified city.
        """
        # Prepare the API request headers
        header = {"apikey": kiwi_key}

        # Prepare the API request parameters
        query = {"term": city_name, "location_types": "city"}

        # Make the API request to get the IATA code
        kiwi_api_locations_query = f"{KIWI_END_POINT}/locations/query"
        response = requests.get(url=kiwi_api_locations_query, headers=header, params=query)

        # Return the IATA code for the specified city
        return response.json()["locations"][0]["code"]

    def search(self, fly_to):
        """
        Performs a flight search from London to a specified destination.

        :param fly_to: The IATA code of the destination.
        """
        # Prepare the API request headers
        header = {"apikey": "I9fMe2Bv0Sur-2O-1ybR7dv0pW3SOztw"}


        # Get today's date and calculate the date range for the flight search
        today = date.today()
        tomorrow = today + timedelta(days=1)
        six_month = tomorrow + timedelta(days=6 * 30)
        tomorrow = tomorrow.strftime("%d/%m/%Y")
        six_month = six_month.strftime("%d/%m/%Y")

        # Prepare the API request parameters for the flight search
        query = {
            "fly_from": "LON",
            "fly_to": fly_to,
            "date_from": tomorrow,
            "date_to": six_month,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "max_stopovers": 0,  # Set this to 0 for direct flights
            "one_for_city": 1,
        }

        # Make the API request to perform the flight search
        kiwi_search_api = f"{KIWI_END_POINT}/search"
        response = requests.get(url=kiwi_search_api, headers=header, params=query)
        data = response.json()["data"][0]

        # Print and store flight information
        print(f"{data['cityTo']}:{data['price']}")
        self.flightdata.add_flight(
            data["cityTo"],
            data["price"],
            fly_to,
            self.timestamp_to_date(data["route"][0]["dTimeUTC"]),
            self.timestamp_to_date(data["route"][1]["dTimeUTC"]),
        )

    def timestamp_to_date(self, timestamp):
        """
        Converts a Unix timestamp to a human-readable date.

        :param timestamp: The Unix timestamp to convert.
        :return: A string representing the date in the format "dd/mm/YYYY".
        """
        # Define the UTC timezone
        utc_timezone = timezone.utc

        # Convert the timestamp to a datetime using the UTC timezone
        dt_utc = datetime.fromtimestamp(timestamp, tz=utc_timezone)

        # Format the datetime as a string in the "dd/mm/YYYY" format
        return dt_utc.strftime("%d/%m/%Y")
