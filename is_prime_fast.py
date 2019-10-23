from math import sqrt
from ip import mersenne_number


def is_prime_fast(number):
    """Checks and returns whether a number is prime."""

    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


# mers_list = [mersenne_number(number)
#              for number in range(3, 66) if is_prime_fast(number) is True]
# print(mers_list)
# for value in mers_list:
#     print(f"{value} is prime: {is_prime_fast(value)}")
