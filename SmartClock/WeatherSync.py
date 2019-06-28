from JsonControl import get_json

url = "http://api.openweathermap.org/data/2.5/weather?id=1835848&APPID=2c0a4bf7e0fd4d5b28a9931ef0a4bb0f"


class WeatherSync:
    _json_weather = None

    def __init__(self) -> None:
        self.sync_weather()

    def sync_weather(self):
        temp_url = url
        # TODO sync weather api
        self.json_weather = get_json(temp_url)

    @property
    def json_weather(self):
        return self._json_weather

    @json_weather.setter
    def json_weather(self, new_json):
        self._json_weather = new_json

    def get_data(self, data):
        return self.json_weather[data]

    def get_weather_main(self):
        data = self.get_data("weather")
        main_id = data[0]["id"]

        return get_condition_by_id(main_id)


def get_condition_by_id(data):
    # Sunny
    if data == 800:
        return 0

    # Cloudy
    if 701 <= data <= 781:
        return 1
    if 801 <= data <= 804:
        return 1

    # Rainy
    if 500 <= data <= 531:
        return 2
    if 300 <= data <= 321:
        return 2
    if 200 <= data <= 232:
        return 2

    # Snowy
    if 600 <= data <= 622:
        return 3
