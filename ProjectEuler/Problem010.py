"""
Project Euler - Problem 010: Summation of primes
"""

import sympy # Far faster than PyPrimes

primes = []
Number = 2000000

for i in range(0, Number):
    if sympy.isprime(i):
        primes.append(i)

print(sum(primes))
