"""
Project Euler - Problem 003: Largest prime factor
"""

# Import relevant libraries
import pyprimes
# Define the number
n = 600851475143
# Print the result of the largest prime factor
print(max(pyprimes.factors(n)))

#####

# Alternatively ...

#####

# Define the number
n = 600851475143

i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
# Print the result
print(n)