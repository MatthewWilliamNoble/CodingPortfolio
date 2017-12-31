"""
Project Euler - Problem 014: Longest Collatz sequence
"""

CountMax = 0

for i in range(1, 1000000):

    j = i
    Count = 0

    while i != 1:

        if i % 2 == 0:
            i = i / 2
            Count += 1
        else:
            i = 3 * i + 1
            Count += 1

    if Count > CountMax:

        CountMax = Count
        print("The number ", j, " with a Count Chain of ", CountMax)
