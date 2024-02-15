'''Testing the calculator class'''
from calculator import calculator

def test_calculator():
    ''' calc add'''
    assert calculator.add(2,2) == 4
    assert calculator.divide(2,2) == 1
    assert calculator.multiply(2,2) == 4
    assert calculator.subtract(3,1) == 2
