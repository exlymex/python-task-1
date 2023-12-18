import requests


class WeatherAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_by_city(self, city_name, days=1):
        params = {'q': city_name, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.base_url, params=params)
        return response.json()
