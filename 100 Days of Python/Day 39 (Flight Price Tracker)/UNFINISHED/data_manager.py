
import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/603cda274a3d468f01c07d4658c44f67/flightDeals/prices'

class DataManager:
    def __init__(self):
        self.new_sheety_data = {}

    def update_sheety_data(self):
        sheety_response = requests.get(SHEETY_PRICES_ENDPOINT)
        sheety_data = sheety_response.json()
        print(sheety_data)
        for i in range(len(sheety_data)):
            self.iataCode = sheety_data[i]['iataCode']
            
            from flight_search import FlightSearch
            flight = FlightSearch()
            flight.get_destination_code()
            if self.iataCode  == '':
                sheety_input = {
                    "price": {
                        "iataCode": flight.code,
                    }
                }

                sheety_update = requests.put(f'{SHEETY_PRICES_ENDPOINT}/{sheety_data[i]["id"]}', json=sheety_input)
                sheety_update.raise_for_status()
        print(sheety_data)
            

