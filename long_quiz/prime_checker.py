from math import sqrt
def is_prime(num:int):
    if num < 2:
        return False
    num_sqrt = sqrt(num)
    primes = [2, 3, 5]
    for i in range(2, int(num_sqrt)):
        if i % 2 == 0:
            pass
        elif i % 3 == 0:
            pass
        elif i % 5 == 0:
            pass
        else:
            primes.append(i)
    for prime in primes:
        if num % prime == 0 and num not in primes:
            return False
        else:
            pass
    return True
