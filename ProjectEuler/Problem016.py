"""
Project Euler - Problem 016: Power digit sum
"""

X = str(2**1000)

Sum = 0

for i in range(len(X)):
    Sum = Sum + int(X[i])

print(Sum)
