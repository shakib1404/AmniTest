import pytest
from calculator import divide, average, fahrenheit_to_celsius

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)          # this will FAIL — agent must fix it

def test_average_empty():
    with pytest.raises(ValueError):
        average([])

def test_fahrenheit_to_celsius_normal():
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0
    assert fahrenheit_to_celsius(68) == 20.0

def test_fahrenheit_to_celsius_negative():
    assert fahrenheit_to_celsius(-40) == -40.0            # this will FAIL — agent must fix it

