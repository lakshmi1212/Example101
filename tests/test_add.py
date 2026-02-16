import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_positive_and_negative():
    assert add(5, -3) == 2

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_add_float_numbers():
    assert add(2.5, 3.1) == pytest.approx(5.6)

def test_add_string_should_fail():
    with pytest.raises(TypeError):
        add('a', 'b')
