# tests/test_generate_prime_factors.py
import pytest
import prime

def test_not_integer():
    # check if string
    with pytest.raises(ValueError):
       prime.generate_prime_factors("string")

   # check if float
    with pytest.raises(ValueError):
        prime.generate_prime_factors(6.66)