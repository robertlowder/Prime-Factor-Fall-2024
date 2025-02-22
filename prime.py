"""
prime.py -- Write the application code here
"""


def generate_prime_factors(num):
    if type(num) != int:
        raise ValueError('Input must be an integer.')
