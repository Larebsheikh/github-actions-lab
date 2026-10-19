import pytest
from calculator import add, subtract, multiply, divide

def test_calc_add():
    assert add(2, 3) == 5

def test_calc_subtract():
    assert subtract(5, 2) == 3

def test_calc_multiply():
    assert multiply(4, 3) == 12

def test_calc_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not permitted."):
        divide(10, 0)
