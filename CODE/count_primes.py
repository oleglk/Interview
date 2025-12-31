# count_primes.py - Count primes less than n using sieve of Eratosthenes.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from count_primes import *

# RELOAD:
# import importlib; import count_primes; importlib.reload(count_primes); from count_primes import *

# The idea:
# Init array isPrime[n] to [false, false, true,..., true]
# Look for (prime) factors p >= 2:
#  foreach marked-as-prime number p from 2 to sqrt(n)
#    mark as non-prime numbers p*p, p*(p+1), p*(p+2), ... n
## Considering primes <= sqrt(n), since a composite number n has at least one factor <= sqrt(n) (mult of 2 numbers > sqrt(n) produce result > n).
## Starting from p*p, since p*(p-1) and smaller are already processed.


def count_primes(n: int) -> int:
    if ( n <= 2 ):
        return 0
    isPrime = [True]*n  # 0 .. n-1
    isPrime[0] = False;  isPrime[1] = False

    p = 2
    while ( p*p < n ):
        if ( not isPrime[p] ):
            p += 1
            continue  # we are only interested in believed-to-be-prime factors
        for i in range(p*p, n, p):  # p*(p+1)==p*p+p; p*(p+2)==p*p+p+p
            isPrime[i] = False
        p += 1

    return sum(isPrime)


def test__count_primes():
    for n in [
            3,  #1
            10, #4
            35  #11
            ]:
        print("====================================")
        print(f"Input: {n}")
        res = count_primes(n)
        print(f"Result: {res}")
