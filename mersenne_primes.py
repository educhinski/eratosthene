from ip import mersenne_number, is_prime, get_primes
from lucas_lehmer import lucas_lehmer


def mersenne_primes_test(exponent):
    """Returns a boolean after testing whether the mersenne number from
    the exponent is prime."""

    mers = mersenne_number(exponent)
    status = is_prime(mers)

    return status


primes_list = get_primes(66)[1:]

for prime in primes_list:
    mers_prime_status = []
    mers_prime_status.append(int(is_prime(mersenne_number(prime))))


list_mers_tups = list(zip(primes_list, mers_prime_status))

print(primes_list)
print(mers_prime_status)
print(list_mers_tups)
