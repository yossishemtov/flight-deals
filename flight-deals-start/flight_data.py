class FlightData:
    def __init__(self):
        self.dicts={}


    def add_flight(self, to_city, price, iataCode, date_arrival, date_departure):
        dict={}
        dict["price"] = price
        dict["iataCode"] = iataCode
        dict["date_arrival"] = date_arrival
        dict["date_departure"] = date_departure
        self.dicts[to_city] = dict
