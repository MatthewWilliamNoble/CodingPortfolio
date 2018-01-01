"""
Project Euler - Problem 022: Names scores
"""

import csv

# Define a letter value ...
# ... Assumes that the values are capitals ...
# ... The int returned is the unicode value.
def NameWorth(Letter):
    return ord(Letter) - 64

# Open the csv file from the DataFiles directory and sort it alphabetically
with open("DataFiles/p022_names.txt","r") as f:
    reader = csv.reader(f)
    for row in reader:
        Data = sorted(row)

NameScore = 0

TotalNameScore = 0

# Cycle through and return individual names ...
# ... then cycle through and return individual letters.
for i in range(len(Data)):

    Name = Data[i]

    LetterScore = 0

    for j in range(len(Name)):
        Letters = Name[j]
        LetterScore = LetterScore + NameWorth(Letters)

    NameScore = (i+1)*LetterScore

    TotalNameScore = TotalNameScore + NameScore

print(TotalNameScore)