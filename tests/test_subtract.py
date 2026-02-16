import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_positive_and_negative():
    assert subtract(5, -3) == 8

def test_subtract_large_numbers():
    assert subtract(2000000, 1000000) == 1000000

def test_subtract_float_numbers():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)

def test_subtract_string_should_fail():
    with pytest.raises(TypeError):
        subtract('a', 'b')
