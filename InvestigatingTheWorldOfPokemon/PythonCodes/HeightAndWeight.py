# Importing the relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
from HomeBrewFunctions import UniqueWordCounter, ListGenerator

##########

# Creating the pandas data frame
Path = r"C:\Users\Matthew\Documents\Pycharm\DataScienceProjects\Pokemon\PokemonData.csv"
df = pd.read_csv(Path, index_col=0)

##########

# Box Plot

plt.figure(1)
plt.boxplot(df["Weight_kg"], labels = ["Weight"])
plt.ylabel("Weight [kg]")
plt.title("Box Plot of Pokémon Weight")

plt.figure(2)
plt.boxplot(df["Height_m"], labels = ["Height"])
plt.ylabel("Height [m]")
plt.title("Box Plot of Pokémon Height")

plt.figure(3)
plt.scatter(df["Weight_kg"],df["Height_m"], alpha=0.5)
plt.ylabel("Height [m]")
plt.xlabel("Weight [kg]")
plt.title("Scatter Plot of Pokémon Height [m] Vs Weight [kg]")

plt.show()

#####

# Correlation Stats Vs parameters

print("+++++CORRELATION+++++")
frame = df[["Total", "HP", "Attack", "Defense", "Sp_Atk", "Sp_Def", "Speed", "Height_m", "Weight_kg"]]
print(round(frame.corr(), 3))

frame = df[["Height_m", "Weight_kg"]]
print(round(frame.describe(), 2))
