import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -2, 1),
    (100, 50, 50),
    (-5, 5, -10),
    (2.5, 1.5, 1.0),
    (1e10, 1e9, 9e9)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract("a", 1)
    with pytest.raises(TypeError):
        subtract(1, "b")
