"""
Project Euler - Problem 023: Non-abundant sums
"""

PerfectNumbers = []
DeficientNumbers = []
AbundantNumbers = []

MAX = 28123

def Factors(x):
    Factors_Array = []
    for i in range(1, x):
        if x % i == 0:
            Factors_Array.append(i)
    return Factors_Array

for i in range(1, MAX + 1):
    if sum(Factors(i)) == i:
        PerfectNumbers.append(i)
    elif sum(Factors(i)) < i:
        DeficientNumbers.append(i)
    elif sum(Factors(i)) > i:
        AbundantNumbers.append((i))

"""
You could just have a list of 28124 boolean values initialized to False. 
Then iterate over the abundant numbers and for each number find the all sums with numbers equal or greater than it. 
For every sum x set the xth flag in the list True. 
Since the abundant numbers are in ascending order you can break the inner loop when sum is greater than 28123. 
Then in the final step iterate over the list and sum together all the indeces which have False value.
"""

result = [False] * (MAX + 1)

for i in range(len(AbundantNumbers)):
    for j in range(i, len(AbundantNumbers)):
        s = AbundantNumbers[i] + AbundantNumbers[j]
        if s > MAX:
            break
        result[s] = True

print(sum(i for i, x in enumerate(result) if not x))
