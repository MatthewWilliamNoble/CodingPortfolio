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

# Initialize an empty dictionary
counts_dict = {}

# Iterate over all of the rows in a column and record the unique word count.
for entry in df["Egg_Group_1"]:
    if entry in counts_dict.keys():
        counts_dict[entry] += 1
    else:
        counts_dict[entry] = 1

for entry in df["Egg_Group_2"]:
    if entry in counts_dict.keys():
        counts_dict[entry] += 1
    else:
        counts_dict[entry] = 1

for key, value in counts_dict.items():
    print(str(key), ":", int(value))

X, Y = ListGenerator(counts_dict)

# Hard coding the removal of NaN
X.remove("nan")
Y.remove(530)

width = 1/3

ax = plt.subplot()

BarPlotGenerations = ax.bar(X, Y, width, color = "blue", zorder=2)

plt.title("Pokémon by Egg Group")
plt.xlabel("Egg Group")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 250])

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