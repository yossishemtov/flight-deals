import requests
# Sheety API endpoint for prices sheet
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/53fb598c35a205adcc4aeada20f6090b/pyhtonFlightDeals/prices"

class DataManager:
    """
    The DataManager class is responsible for managing data operations, including fetching, updating,
    and interacting with the Sheety API to retrieve and update destination information.
    """

    def __init__(self):
        """
        Initializes a new instance of the DataManager class.
        """
        # Destination data storage
        self.destination_data = {}

    def get_destination_data(self):
        """
        Fetches destination data from the Sheety API.

        :return: A list containing destination data.
        """
        # Make a GET request to the Sheety API to retrieve destination data
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()

        # Update the destination_data attribute with the fetched data
        self.destination_data = data["prices"]

        # Return the fetched destination data
        return self.destination_data

    def update_destination_codes(self):
        """
        Updates destination IATA codes in the Google Sheet using the Sheety API.

        This method iterates through the destination data and makes a PUT request for each entry
        to update the IATA code in the Google Sheet.
        """
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            # Make a PUT request to update the IATA code in the Google Sheet
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

    def update_destination_price(self, price, id):
        """
        Updates the lowest price for a destination in the Google Sheet using the Sheety API.

        :param price: The new lowest price for the destination.
        :param id: The ID of the destination row in the Google Sheet.
        """
        # Print the information about the price update
        print(f"{id} price: {price}")

        # Prepare the new data to be updated in the Google Sheet
        new_data = {
            "price": {
                "lowestPrice": price
            }
        }

        # Make a PUT request to update the lowest price in the Google Sheet
        response = requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{id}",
            json=new_data
        )
        # Print the status code of the PUT request
        print(response.status_code)
