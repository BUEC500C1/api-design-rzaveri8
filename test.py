import weather-api
import pytest


# content of test_class.py
class TestClass:
    def test_exist(self):
        result = hasattr(int2roman, 'int_to_Roman')
        assert result, "Function does not exist!"
    def test_correct(self):
        result = int2roman.int_to_Roman(4)
        assert result == "IV"
    def test_correct(self):
        result = int2roman.int_to_Roman(70000)
        assert result == "LXX"
    def test_neg(self):
        result = int2roman.int_to_Roman(-4)
        assert result == "ERROR: Not a positive integer"
    def test_string(self):
        result = int2roman.int_to_Roman('hello')
        assert result == "ERROR: Not an integer"
    def test_value(self):
        result = int2roman.int_to_Roman(8910394)
