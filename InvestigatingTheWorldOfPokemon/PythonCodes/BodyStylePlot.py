# Importing the relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
from HomeBrewFunctions import UniqueWordCounter, ListGenerator

##########

# Creating the pandas data frame
Path = r"C:\Users\Matthew\Documents\Pycharm\DataScienceProjects\Pokemon\PokemonData.csv"
df = pd.read_csv(Path, index_col=0)

##########

# Bar Plot

dic = UniqueWordCounter("PokemonData.csv", "Body_Style")

X, Y = ListGenerator(dic)

width = 1/3

ax = plt.subplot()

BarPlotGenerations = ax.bar(X, Y, width, color = "blue", zorder=2)

plt.title("Pokémon by Body Style")
plt.xlabel("Body Style")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 200])

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