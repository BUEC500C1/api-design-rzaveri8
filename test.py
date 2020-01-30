import weather_api
import pytest


# content of test_class.py
class TestClass:
    # tests for airport code input
    def test_exist(self):
        result = hasattr(weather_api, 'getAirportLoc')
        assert result, "Function does not exist!"
    def test_correct(self):
        result = weather_api.getAirportLoc('AES')
        assert result =='Aalesund, Norway '
    def test_false(self):
        result = weather_api.getAirportLoc(7)
        assert result == "ERROR: Not a String"

    #tests for weather api output
    def test_exist(self):
        result = hasattr(weather_api, 'getWeather')
        assert result, "Function does not exist!"
    def test_correct(self):
        result = weather_api.getWeather('adsfsdfdsfs')
        assert result =='City not found, please try again'
    def test_correct(self):
        result = weather_api.getWeather('adsfsdfdsfs')
        assert result != 'City not found, please try again'
    def test_false(self):
        result = weather_api.getWeather(7)
        assert result == "Error: Not a string"
