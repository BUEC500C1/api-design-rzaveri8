import weather_api
import pytest


# content of test_class.py
class TestClass:
    # tests for airport code input
    def test_airport_exist(self):
        result = hasattr(weather_api, 'getAirportLoc')
        assert result, "Function does not exist!"
    def test_airport_correct(self):
        result = weather_api.getAirportLoc('AES')
        assert result =='Aalesund, Norway '
    def test_airport_false(self):
        result = weather_api.getAirportLoc(7)
        assert result == "ERROR: Not a String"

    #tests for city parser


    #tests for weather api output
    def test_weather_exist(self):
        result = hasattr(weather_api, 'getWeatherDescription')
        assert result, "Function does not exist!"
    def test_weather_correct(self):
        result = weather_api.getWeatherDescription('adsfsdfdsfs')
        assert result =="ERROR: City not found, please try again"
    def test_weather_false(self):
        result = weather_api.getWeatherDescription(7)
        assert result == "ERROR: Not a string"
