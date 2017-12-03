"""
Project Euler - Problem 009: Special Pythagorean triplet
"""

import sys

for i in range(1, 1000):
    for j in range(1, 1000):
        for k in range(1, 1000):
            if i + j + k == 1000 and i**2 + j**2 == k**2:
                a = i
                b = j
                c = k
                Product = a * b * c
                print(Product)

                sys.exit("FOUND IT!")