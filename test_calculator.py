import pytest
from calculator import Calculator

def test_add():
    calculator = Calculator()
    assert calculator.add(4, 6) == 10
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(-1, 1) == -2
    assert calculator.subtract(0, 0) == 0

def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(0, 5) == 0

def test_divide():
    calculator = Calculator()
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-6, 3) == -2
    with pytest.raises(ValueError):
        calculator.divide(6, 0)
        
def test_power():
    calculator = Calculator()
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(0, 5) == 0
    
def test_logarithm():
    calc = Calculator()
    assert calc.logarithm(8, 2) == 3
    assert calc.logarithm(1000, 10) == pytest.approx(3, rel=1e-9)
