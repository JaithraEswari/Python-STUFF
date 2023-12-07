import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "Bw268ltB9WJ6NhSdTAa5qj6x5zEshSZh"

class FlightSearch:
    def __init__(self):
        city = 'TESTING'
        self.city = city