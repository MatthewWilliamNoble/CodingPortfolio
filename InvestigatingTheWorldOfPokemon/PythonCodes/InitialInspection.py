# Importing the relevant libraries
import pandas as pd
from HomeBrewFunctions import NaN_Counter, NaN_Checker

#####

# Creating the pandas data frame
Path = r"C:\Users\Matthew\Documents\Pycharm\DataScienceProjects\Pokemon\PokemonData.csv"
df = pd.read_csv(Path, index_col=0)

#####

# Confirming the headings and looking at how the fields are entered.
print("\n", "+++++DataFrame Head")
print(df.head())

#####

# Are there any NaN values?
NaN_Checker(df)

#####

# Where are they?
NaN_Counter(df)
