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

def test_input_3():
    # check that the list [3] is returned if
    # generate_prime_factors is called with a 3
    assert prime.generate_prime_factors(3) == [3]

def test_input_4():
    # check that the list [4] is returned if
    # generate_prime_factors is called with a 3
    assert prime.generate_prime_factors(4) == [2,2]

def test_input_6():
    # check that the list [4] is returned if
    # generate_prime_factors is called with a 3
    assert prime.generate_prime_factors(6) == [2,3]

def test_input_7():
    # check that the list [4] is returned if
    # generate_prime_factors is called with a 3
    assert prime.generate_prime_factors(8) == [2,2,2]

def test_input_9():
    # check that the list [4] is returned if
    # generate_prime_factors is called with a 3
    assert prime.generate_prime_factors(9) == [3,3]