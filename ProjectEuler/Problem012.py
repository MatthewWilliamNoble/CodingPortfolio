"""
Project Euler - Problem 012: Highly divisible triangular number
"""

# Define a triangle Number
def triangular(n):
    return (n*(n+1))/(2)

# Define a factorisation function
def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

# Search for the relevant number
for i in range(1, 10**100):
    if len(factors(triangular(i))) > 500:
        print(triangular(i))
        break