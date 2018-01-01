"""
Project Euler - Problem 020: Factorial digit sum
"""

import math

n = math.factorial(100)

N = str(n)

Sum = 0

for i in range(len(N)):
    Sum = Sum + int(N[i])

print(Sum)
