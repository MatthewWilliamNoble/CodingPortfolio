"""
Project Euler - Problem 025: 1000-digit Fibonacci number
"""

# Function to define the Fibonaii numbers

ListofFibNumbers = {0:0, 1:1}

def Fib(n):
    if not n in ListofFibNumbers:
        ListofFibNumbers[n] = Fib(n-1) + Fib(n-2)
    return ListofFibNumbers[n]

# Iterate upwards until the length of the number is 1000 digits long.

i = 0

while len(str(Fib(i))) < 1000:
    Fib(i)
    i = i + 1

print(i)
