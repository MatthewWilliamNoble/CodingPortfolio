import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from HomeBrewFunctions import UniqueWordCounter, ListGenerator

#Who has Gender?
Gender = UniqueWordCounter("PokemonData.csv" ,"hasGender")
PrMale = UniqueWordCounter("PokemonData.csv" ,"Pr_Male")

Gender_Key, Gender_Val = ListGenerator(Gender)
PrMale_Key, PrMale_Val = ListGenerator(PrMale)

#####

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = Gender_Key
sizes = Gender_Val
explode = (0.1, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Pie Chart of the Pokémon with (True) and without (False) Gender")

#####

plt.figure(2)

X = ["0.00", "0.125", "0.25", "0.50", "0.75", "0.875", "NaN", "1.00"]
Y = [23, 2, 22, 458, 19, 101, 77, 19]
width = 1/3

ax = plt.subplot()
BarPlotGenerations = ax.bar(X, Y, width, color = "blue", zorder=2)

plt.title("A Pokémon's Probability of Being Male")
plt.xlabel("Probability")
plt.ylabel("Number of Pokémon")
#plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 550])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPlotGenerations, ax)

plt.show()

plt.show()
