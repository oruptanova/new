import pytest
from pytest import approx
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0)
])
def test_add(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (10, 5, 5)
])
def test_subtract(a, b, expected):
    calc = Calculator()
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 5, -10)
])
def test_multiply(a, b, expected):
    calc = Calculator()
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (10, 0, ValueError)
])
def test_divide(a, b, expected):
    calc = Calculator()
    if expected == ValueError:
        with pytest.raises(ValueError):
            calc.divide(a, b)
    else:
        assert calc.divide(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (5, 0, 1)
])
def test_power(a, b, expected):
    calc = Calculator()
    assert calc.power(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (8, 2, 3),
    (1000, 10, 3)
])
def test_logarithm(a, b, expected):
    calc = Calculator()
    assert calc.logarithm(a, b) == approx(expected)
