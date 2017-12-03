"""
Project Euler - Problem 002: Even Fibonacci numbers
"""

FibNumDic = {0:0, 1:1}

# Function to calculate the nth Fibonacci number
def Fib(n):
    if not n in FibNumDic:
        FibNumDic[n] = Fib(n-1) + Fib(n-2)
    return FibNumDic[n]

# Generate all Fibonacci numbers less than 4M in size
i=2
while Fib(i) < 4000000:
    Fib(i)
    i += 1

# Summation loop of even numbers
Sum = 0
for keys, values in FibNumDic.items():
    if values % 2 == 0:
        Sum += values

# Print the result
print(Sum)