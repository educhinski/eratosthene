"""Mersenne Numbers"""

from math import log10 as log, sqrt as sr


def is_prime(number):
    """Checks if the passed number is a prime."""
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_primes(upto):
    "Returns a list of primes up to the given value."
    return [i for i in range(2, upto) if is_prime(i) is True]


def is_mersenne(number):
    """Checks for mesenne numbers, numbers that take the form 2**p - 1"""
    p = log(number + 1)/log(2)
    if p.is_integer() is False:
        return False
    return True


def mersenne_number(exponent):
    "Returns a mersenne number when the exponent is passed."
    return 2**exponent - 1


def get_mersenne(num):
    """Returns the mersenne combination."""
    exponent = log(num + 1) / log(2)
    return f"2^{exponent} + 1"


# some_primes = get_primes(66)[1:]
# print(f"The primes are :\n {some_primes}")

# some_primes_mersenne = [mersenne_number(i) for i in some_primes]
# print(f"The primes mersenne numbers are :\n {some_primes_mersenne}")

# mersenne_combination = [get_mersenne(i) for i in some_primes]
# print(f"The mersenne combinations are: \n{mersenne_combination}")

# # print([True for j in some_primes_mersenne if is_prime(j) == True])

# trials = [is_7%
