
import pytest


@pytest.mark.basic
def test_one_plus_one():
    assert 1 +1 == 2

@pytest.mark.basic    
def test_one_plus_two():
    a= 1
    b= 2
    c = 3
    assert a + b == c

products =[
    (2,3,6),
    (1,99,99),
    (0,99,0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

@pytest.mark.parametrize('a, b, product',products)
def test_multiplication(a,b, product):
    assert a * b == product