import weather_api
import pytest
import sample_config
from helper_funcs import getAirportLoc
from helper_funcs import getCity



# content of test_class.py
#tests.
class TestClass:
    # tests for airport code input
    def test_airport_exist(self):
        result = hasattr(helper_funcs, 'getAirportLoc')
        assert result, "Function does not exist!"
    def test_airport_correct(self):
        result = getAirportLoc('AES')
        assert result =='Aalesund, Norway '
    def test_airport_false(self):
        result = getAirportLoc(7)
        assert result == "ERROR: Not a String"

    #tests for weather api output
    def test_city_exist(self):
        result = hasattr(helper_funcs, 'getCity')
        assert result, "Function does not exist!"
    def test_city_correct(self):
        result = getCity(42)
        assert result =="ERROR: Not a String"
