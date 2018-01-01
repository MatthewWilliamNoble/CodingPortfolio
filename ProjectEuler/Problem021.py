"""
Project Euler - Problem 020: Amicable numbers
"""

# Factor function (not including itself)

def Factors(x):
    Factors_Array = []
    for i in range(1, x):
        if x % i == 0:
            Factors_Array.append(i)
    return Factors_Array

AmicableNumbers_Array = []

for i in range(1, 10000):

    A = sum(Factors(sum(Factors(i))))
    B = sum(Factors(i))
    if A == i and i != B:
        #print(i, B)
        AmicableNumbers_Array.append(i)

print(sum(AmicableNumbers_Array))