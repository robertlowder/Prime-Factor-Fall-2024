"""
prime.py -- Write the application code here
"""


def generate_prime_factors(num):

    # if function is sent anything other than an integer, raise ValueError message
    if type(num) != int:
        raise ValueError('Input must be an integer.')

    # if function is sent a 1 return an empty List
    if num == 1:
        return []