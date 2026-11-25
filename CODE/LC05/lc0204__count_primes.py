# lc0204__count_primes.py
# Given an integer n, return the number of prime numbers that are strictly less than n.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0204__count_primes import *

# RELOAD:
# import importlib;    import lc0204__count_primes;  importlib.reload(lc0204__count_primes);  from lc0204__count_primes import *

# The idea: Sieve of Eratosthenes algorithm - init bool isPrime array to True from #2 up; starting from 2 and till n-1, if still marked as prime, mark all its multiples < n as non-prime.
# See: https://algo.monster/liteproblems/204


def count_primes(n: int) -> int:
    if ( n <= 2 ):
        return 0  # no primes below 2
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    cntPrimes = 0
    for candidate in range(2, n):
        if ( not isPrime[candidate] ):
            continue
        cntPrimes += 1
        # mark all 'candidate's multiples < n as non-prime
        for multiple in range(2*candidate, n, candidate):
            isPrime[multiple] = False
    return cntPrimes
##


def test__count_primes():
    tasks = [
        10,  # 4
        0,   # 0
        1,   # 0
    ]
    for n in tasks:
        print("====================================")
        print(f"Input: {n}")
        res = count_primes(n)
        print(f"Result: {res}")
##
