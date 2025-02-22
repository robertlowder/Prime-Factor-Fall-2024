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


def test_input_1():
    # check that an empty list is returned
    # generate_prime_factors is called with a 1
    assert prime.generate_prime_factors(1) == []


def test_input_2():
    # check that the list [2] is returned if
    # generate_prime_factors is called with a 2
    assert prime.generate_prime_factors(2) == [2]
