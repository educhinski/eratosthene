from is_prime_fast import is_prime_fast
from ip import get_primes


def list_true(upto):
    """Make a list of true values of length n+1"""

    list_true = []
    for i in range(upto + 1):
        if i == 0 or i == 1:
            list_true.append(False)
        else:
            list_true.append(True)

    return list_true


def mark_false(bool_list, p):
    """Marks all elements 2p, 3p ...n false."""

    for p in range(p, len(bool_list)):
        for i in range(p + 1, len(bool_list)):
            if i % p == 0:
                bool_list[i] = False

    return bool_list


def find_next(bool_list, p):
    """Finds and returns the smallest element in a list which is not false and
    is greater than p."""

    next_value = None
    for i in range(len(bool_list)):
        if bool_list[i] is True and i > p:
            next_value = i
            break
    return next_value


def prime_from_list(bool_list):
    """Returns the prime numbers from the edited list of booleans."""

    return [i for i in range(len(bool_list)) if bool_list[i] is True]


def sieve(n):
    """
    The Erastosthenes's sieve for prime numbers.
    Returns a list of prime numbers.
    """

    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)


# assert len(list_true(20)) == 21
# assert list_true(20)[0] is False
# assert list_true(20)[1] is False
# assert mark_false(list_true(6), 2) == [
#     False, False, True, True, False, True, False]
# assert find_next([True, True, True, True], 2) == 3
# assert find_next([True, True, True, False], 2) is None
# assert prime_from_list([False, False, True, True, False]) == [2, 3]
assert sieve(1000) == get_primes(1000)
