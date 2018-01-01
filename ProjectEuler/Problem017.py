"""
Project Euler - Problem 017: Number letter counts
"""

import inflect

p = inflect.engine()

Array = []

for i in range(1, 1001):
    X = p.number_to_words(i)
    Array.append(X)

#Scrubbing spaces and hyphens

for i in range(len(Array)):
    Y = Array[i]
    Y = Y.replace("-", "")
    Y = Y.replace(" ", "")
    Array[i] = Y

Sum = 0

for i in range(len(Array)):
    Sum = Sum + len(Array[i])

print(Sum)




