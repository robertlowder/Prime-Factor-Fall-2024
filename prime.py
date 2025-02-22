"""
prime.py -- Write the application code here
"""

def generate_prime_factors(num):

    # if function is sent anything other than an integer, raise ValueError message
    if type(num) != int:
        raise ValueError('Input must be an integer.')

    # if function is sent a 1 return an empty List
    if num < 2:
        return []


    # if function is sent a number 2 or greater it will run this algorithm to
    # break it down into its prime factors and append each one to a list until
    # there are no more left and then return the factored list
    factors = []
    divisor = 2

    while num >= divisor:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor +=1
    return factors


# User Interface
user_input = input('Please enter an integer to be factored into primes: ').strip()

while True:
    try:
        value = int(user_input)
        print(generate_prime_factors(value))
        break

    except ValueError:
        user_input = input('Invalid input.\n'
                           'Please enter an integer to be factored into primes: ').strip()



