from data_manager import DataManager
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "obJNu84iftgNq297B38Xkg6T0Vdh3wUz"

class FlightSearch():
    def __init__(self):
        pass
    def get_destination_code(self):
        data = DataManager()
        data.update_sheety_data()
        city_code = data.iataCode
        header = {
            'apikey': TEQUILA_API_KEY,
        }

        input = {
            'term': city_code,
            'location': 'city',
        }

        flight_search_response = requests.get(f'{TEQUILA_ENDPOINT}/locations/query',json = input, headers=header,)
        flight_search_response.raise_for_status()
        flight_search_data = flight_search_response.json()
        self.code = flight_search_data['locations'][0]['code']
        return self.code

