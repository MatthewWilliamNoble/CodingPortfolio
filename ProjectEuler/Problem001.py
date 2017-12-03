"""
Project Euler - Problem 001: Multiples of 3 and 5
"""

# Summation loop of multiples of 3 and 5
Sum = 0
for i in range(1, 1000):
    if not i % 3 or not i % 5:
        Sum += i

# Print the result
print (Sum)