from src.app import app, calculate
from src.operators import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2,3) == 5

def test_add0():
    assert add(2,0) == 2

def test_sub():
    assert subtract(2,3) == -1

def test_sub0():
    assert add(2,0) == 2

def test_mul():
    assert multiply(2,3) == 6

def test_mul0():
    assert multiply(2,0) == 0

def test_div():
    assert divide(2,3) == 2/3

def test_div0():
    with pytest.raises(ZeroDivisionError):
            divide(2, 0)
def test_calculate_add():
    assert calculate("10+5") == 15

def test_calculate_mul():
    assert calculate("10*5") == 50

def test_calculate_div():
    assert calculate("10/5") == 2

def test_calculate_sub():
    assert calculate("10-5") == 5