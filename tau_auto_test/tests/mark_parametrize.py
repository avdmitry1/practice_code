import pytest

product = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75),
]

@pytest.mark.parametrize('a, b, product', product)
def test_multiplication(a, b, product):
    assert a * b == product
    