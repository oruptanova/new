# test_calculator.py

import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_addition(calculator):
    assert calculator.add(2, 3) == 5

def test_subtraction(calculator):
    assert calculator.subtract(5, 3) == 2

def test_multiplication(calculator):
    assert calculator.multiply(2, 3) == 6

def test_division(calculator):
    assert calculator.divide(6, 2) == 3

def test_division_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(6, 0)