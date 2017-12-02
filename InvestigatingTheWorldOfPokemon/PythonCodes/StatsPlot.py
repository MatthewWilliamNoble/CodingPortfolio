import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##########

# Creating the pandas data frame
Path = r"C:\Users\Matthew\Documents\Pycharm\DataScienceProjects\Pokemon\PokemonData.csv"
df = pd.read_csv(Path, index_col=0)

##########

plt.figure(1)
plt.boxplot([df["HP"], df["Attack"], df["Defense"], df["Sp_Atk"], df["Sp_Def"], df["Speed"]], 0, labels=["HP", "Attack", "Defence", "Sp. Attack", "Sp. Defence", "Speed"])
plt.xticks(rotation = "vertical")
plt.ylabel("Base Stat Value")
plt.title("Box Plot of the Base Stats")

plt.figure(2)
plt.boxplot(df["Total"], 0, labels=["Total"])
plt.ylabel("Base Stat Value")
plt.title("Box Plot of the Base Stat: Total")
plt.show()

plt.show()