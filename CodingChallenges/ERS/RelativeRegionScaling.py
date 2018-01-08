# Import the relevant libraries with their usual aliases
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# Set the random number for reproducibility
np.random.seed(42)

"""
# Linear interpolation to rescale between 1 and 99 relative to the other region values
https://en.wikipedia.org/wiki/Linear_interpolation
"""

"""
# Testing
"""

value = 5
lower_old = 0
higher_old = 10
lower_new = 0       # 1
higher_new = 100        # 99

X_linInt = int((value - lower_old)*((higher_new - lower_new)/(higher_old - lower_old))+(lower_new))

#print(X_linInt)

"""
# Building it into a function
"""

def LinearInterpolationINTEGER(Value, OldMin, OldMax, NewMin, NewMax):
    return int((Value - OldMin)*((NewMax - NewMin)/(OldMax - OldMin))+(NewMin))

#print(LinearInterpolationINTEGER(5, 0, 10, 0, 100))

# Testing on a random array
array = np.random.random(size=10)
array = list(array)

#print(array)
#print(min(array))
#print(max(array))

# Performing the function on each array element

for i in range(len(array)):
    print(LinearInterpolationINTEGER(array[i], min(array), max(array), 1, 99))

# Testing on a random array with a far larger number
array.append(15)

for i in range(len(array)):
    print(LinearInterpolationINTEGER(array[i], min(array), max(array), 1, 99))

"""
# Doing it with a pandas DataFrame
"""

# Import the data set
iris = load_iris()

# create the data frame
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

#print(data1.head())

ListToAdd = []
MIN = min(data1["sepal length (cm)"])
MAX = max(data1["sepal length (cm)"])

for index, row in data1.iterrows():
    ListToAdd.append(LinearInterpolationINTEGER(row["sepal length (cm)"], MIN, MAX, 1, 99))

print(data1.head())

# Adding the data to the data frame
data1["Test"] = ListToAdd

print(data1.head())