"""
Project Euler - Problem 019: Counting Sundays
"""

import calendar

"""
calendar.monthrange(year, month)
Returns weekday of first day of the month and number of days in month, for the specified year and month.
"""

print(calendar.monthrange(1990, 1))

Count = 0

for i in range(1901, 2001):
    for j in range(1, 13):
        if calendar.monthrange(i, j)[0] == 6:
            Count = Count + 1

print(Count)