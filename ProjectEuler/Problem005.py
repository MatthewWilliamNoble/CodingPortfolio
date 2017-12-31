"""
Project Euler - Problem 005: Smallest multiple
"""

import math

N = 20
check_list = list(range(1 , N + 1))

# Question specific: Faster if we start at N = 2520 and step in 2520's
def findSolution(step):
    for num in range(2520, math.factorial(N) + 1, 2520):
        if all(num % n == 0 for n in check_list):
            return num
    return None

#def find_solution(step):
#    for num in range(N, math.factorial(N) + 1, N):
#        if all(num % n == 0 for n in check_list):
#            return num
#    return None

print(findSolution(N))