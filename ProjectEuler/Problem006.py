"""
Project Euler - Problem 006: Sum square difference
"""

NaturalNumbers = 100
SumOfSquare = 0
power = 2

for i in range(1, NaturalNumbers+1):
    SumOfSquare = SumOfSquare + i**power

List = range(1, NaturalNumbers+1)

Sum = sum(List)
SquareOfSum = Sum**2

ANSWER = SquareOfSum - SumOfSquare

print(ANSWER)

#####

# Or alternatively ...

#####

print(sum(range(1, 101))*sum(range(1, 101)) - sum(i*i for i in range(1, 101)))