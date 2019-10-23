from ip import is_prime, is_mersenne, get_primes, get_mersenne, mersenne_number

# get primes between 3 and 65

the_primes = [i for i in range(3, 66) if is_prime(i) is True]
the_primes2 = get_primes(65)[1:]

print(the_primes)
print(len(the_primes))

print(the_primes2)
print(len(the_primes2))

# for item in the_primes:
#     if is_mersenne:
#         print(f"{item} is mersenne")
#     else:
#         print(f"{item} is not mersenne")

mersennes = [mersenne_number(i) for i in the_primes]
print(mersennes)
print(len(mersennes))
