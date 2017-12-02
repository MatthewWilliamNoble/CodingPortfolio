''' Plotting the total Pokémon per generation using matplotlib'''

# Importing the relevant libraries
import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use('ggplot')

##########

# Creating the pandas data frame
Path = r"C:\Users\Matthew\Documents\Pycharm\DataScienceProjects\Pokemon\PokemonData.csv"
df = pd.read_csv(Path, index_col=0)

##########

# Sub-dividing into the relevant generations
Gen1 = df["Generation"] == 1
Gen2 = df["Generation"] == 2
Gen3 = df["Generation"] == 3
Gen4 = df["Generation"] == 4
Gen5 = df["Generation"] == 5
Gen6 = df["Generation"] == 6

Gen1Poke = df.loc[Gen1]
Gen2Poke = df.loc[Gen2]
Gen3Poke = df.loc[Gen3]
Gen4Poke = df.loc[Gen4]
Gen5Poke = df.loc[Gen5]
Gen6Poke = df.loc[Gen6]

# Bar Plot
Y = [len(Gen1Poke), len(Gen2Poke), len(Gen3Poke), len(Gen4Poke), len(Gen5Poke), len(Gen6Poke)]
X = ["Gen1", "Gen2", "Gen3", "Gen4", "Gen5", "Gen6"]

width = 1/3

ax = plt.subplot()

BarPlotGenerations = ax.bar(X, Y, width, color = "blue", zorder=2)

plt.title("Pokémon by Generation")
plt.xlabel("Generation")
plt.ylabel("Number of Pokémon")
#plt.xticks(rotation="vertical")
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