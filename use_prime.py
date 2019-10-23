def is_prime(number):
    """Checks if the passed number is a prime."""
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


prime_list = [i for i in range(3, 66) if is_prime(i) is True]
mers_list = [2**i - 1 for i in prime_list]
print(prime_list)
print(mers_list)
# print(is_prime(29**2 - 1))
print(is_prime(mers_list[-1]))
