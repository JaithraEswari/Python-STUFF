
import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/603cda274a3d468f01c07d4658c44f67/flightDeals/prices'

class DataManager:
    def __init__(self):
        self.new_sheety_data = {}

    def update_sheety_data(self):
        sheety_response = requests.get(SHEETY_PRICES_ENDPOINT)
        sheety_data = sheety_response.json()['prices']
        for i in range(len(sheety_data)):
            iataCode = sheety_data[i]['iataCode']
            from flight_search import FlightSearch
            self.flight = FlightSearch()
            if iataCode == '':
        #         iataCode = self.flight.city
        # print(sheety_data)
                sheety_input = {
                    "price": {
                        "iataCode": self.flight.city
                    }
                }

                sheety_update = requests.put(f'{SHEETY_PRICES_ENDPOINT}/{sheety_data[i]["id"]}', json=sheety_input)
                sheety_update.raise_for_status()
        # print(sheety_data.json())
            

