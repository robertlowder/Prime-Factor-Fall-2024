# tests/test_generate_prime_factors.py
import pytest
import prime
from prime import generate_prime_factors


def test_not_integer():
    # check if string
    with pytest.raises(ValueError):
       prime.generate_prime_factors("string")

   # check if float
    with pytest.raises(ValueError):
        prime.generate_prime_factors(6.66)

def test_input_1():
    # check that an empty list is returned if a 1 is entered
    assert generate_prime_factors(1) == []