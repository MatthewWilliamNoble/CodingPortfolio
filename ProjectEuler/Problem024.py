"""
Project Euler - Problem 024: Lexicographic permutations
"""

import itertools

X = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

X = sorted(X)

print(X[999999])