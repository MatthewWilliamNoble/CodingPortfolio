import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#####

# Creating the pandas data frame
Path = r"C:\Users\Matthew\Documents\Pycharm\DataScienceProjects\Pokemon\PokemonData.csv"
df = pd.read_csv(Path, index_col=0)

#####

Legendary = df["isLegendary"] == True

Gen1 = df["Generation"] == 1
Gen2 = df["Generation"] == 2
Gen3 = df["Generation"] == 3
Gen4 = df["Generation"] == 4
Gen5 = df["Generation"] == 5
Gen6 = df["Generation"] == 6

Gen1Legendary = df.loc[np.logical_and(Gen1, Legendary)]
Gen2Legendary = df.loc[np.logical_and(Gen2, Legendary)]
Gen3Legendary = df.loc[np.logical_and(Gen3, Legendary)]
Gen4Legendary = df.loc[np.logical_and(Gen4, Legendary)]
Gen5Legendary = df.loc[np.logical_and(Gen5, Legendary)]
Gen6Legendary = df.loc[np.logical_and(Gen6, Legendary)]

#####

# Plotting the Legendaries
Y = [len(Gen2Legendary), len(Gen2Legendary), len(Gen3Legendary), len(Gen4Legendary), len(Gen5Legendary), len(Gen6Legendary)]
X = ["Gen1", "Gen2", "Gen3", "Gen4", "Gen5", "Gen6"]
width = 1/3

ax = plt.subplot()

BarPlotLegendary = ax.bar(X, Y, width, color = "blue", zorder = 2)

plt.title("Legendary Pokemon by Generation")
plt.xlabel("Generation")
plt.ylabel("Number of Pokemon")
plt.grid(linestyle="-", linewidth=0.25, zorder = 0)
plt.ylim([0, 15])

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

autolabel(BarPlotLegendary, ax)

#####

plt.figure(2)
df.boxplot(column = ["HP", "Attack", "Defense", "Sp_Atk", "Sp_Def", "Speed"], labels=["HP", "Attack", "Defence", "Sp. Attack", "Sp. Defence", "Speed"])
plt.xticks(rotation = "vertical")
plt.ylabel("Base Stat Value")
plt.title("Box Plot of the Base Stats (Legendary Overlay)")

y = df[Legendary].HP.dropna()
x = np.random.normal(1, 0.025, size=len(y)) # Add some random "jitter" to the x-axis. Turned off for this plot
plt.plot(x, y, 'r.', alpha=0.5)

y = df[Legendary].Attack.dropna()
x = np.random.normal(2, 0.025, size=len(y)) # Add some random "jitter" to the x-axis. Turned off for this plot
plt.plot(x, y, 'r.', alpha=0.5)

y = df[Legendary].Defense.dropna()
x = np.random.normal(3, 0.025, size=len(y)) # Add some random "jitter" to the x-axis. Turned off for this plot
plt.plot(x, y, 'r.', alpha=0.5)

y = df[Legendary].Sp_Atk.dropna()
x = np.random.normal(4, 0.025, size=len(y)) # Add some random "jitter" to the x-axis. Turned off for this plot
plt.plot(x, y, 'r.', alpha=0.5)

y = df[Legendary].Sp_Def.dropna()
x = np.random.normal(5, 0.025, size=len(y)) # Add some random "jitter" to the x-axis. Turned off for this plot
plt.plot(x, y, 'r.', alpha=0.5)

y = df[Legendary].Speed.dropna()
x = np.random.normal(6, 0.025, size=len(y)) # Add some random "jitter" to the x-axis. Turned off for this plot
plt.plot(x, y, 'r.', alpha=0.5)

#####

plt.figure(3)
df.boxplot(column = "Total", labels= ["Total"])
plt.ylabel("Base Stat Value")
plt.title("Box Plot of the Base Stat: Total (Legendary Overlay)")

y = df[Legendary].Total.dropna()
x = np.random.normal(1, 0.025, size=len(y)) # Add some random "jitter" to the x-axis. Turned off for this plot
plt.plot(x, y, 'r.', alpha=0.5)

plt.show()