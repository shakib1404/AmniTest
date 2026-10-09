import pytest
from calculator import divide, average, power

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)          # this will FAIL — agent must fix it

def test_average_empty():
    with pytest.raises(ValueError):
        average([])            # this will FAIL — agent must fix it

def test_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1
    assert power(2, -1) == 0.5

