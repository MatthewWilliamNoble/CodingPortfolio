
import pandas as pd
import numpy as np
from HomeBrewFunctions import UniqueWordCounter, ListGenerator

##########

# Creating the pandas data frame
Path = r"C:\Users\Matthew\Documents\Pycharm\DataScienceProjects\Pokemon\PokemonData.csv"
df = pd.read_csv(Path, index_col=0)

##########

# How many Pokémon are there?
print("+++++LENGTH+++++")
print(len(df))

##########

#How many types are there?
UniqueWordCounter("PokemonData.csv", "Type_1")

##########

# Correlation between the base stats.
print("+++++CORRELATION+++++")
print(round(df[df.columns[3:10]].corr(), 3))

##########

# Describe the base stats
print("+++++DESCRIBE+++++")
BaseStats = ["Total", "HP", "Attack", "Defense", "Sp_Atk", "Sp_Def", "Speed"]
print(round(df[df.columns[3:10]].describe(), 0))
##########

#How many types are there?
UniqueWordCounter("PokemonData.csv", "Type_1")

##########

#How many Colours are there?
UniqueWordCounter("PokemonData.csv", "Color")

##########

#How many Egg Groups are there?
UniqueWordCounter("PokemonData.csv", "Egg_Group_1")

##########

#How many Body Styles are there?
UniqueWordCounter("PokemonData.csv", "Body_Style")

#####

# Who is the strongest?
# Total
S = df.nlargest(5, "Total")
print(S.iloc[:, [0, 3]])

# Total
S = df.nlargest(5, "HP")
print(S.iloc[:, [0, 4]])

# Total
S = df.nlargest(5, "Attack")
print(S.iloc[:, [0, 5]])

# Total
S = df.nlargest(5, "Defense")
print(S.iloc[:, [0, 6]])

# Total
S = df.nlargest(5, "Sp_Atk")
print(S.iloc[:, [0, 7]])

# Total
S = df.nlargest(5, "Sp_Def")
print(S.iloc[:, [0, 8]])

# Total
S = df.nlargest(5, "Speed")
print(S.iloc[:, [0, 9]])

#####

# Who is the weakest?
# Total
S = df.nsmallest(5, "Total")
print(S.iloc[:, [0, 3]])

# Total
S = df.nsmallest(5, "HP")
print(S.iloc[:, [0, 4]])

# Total
S = df.nsmallest(5, "Attack")
print(S.iloc[:, [0, 5]])

# Total
S = df.nsmallest(5, "Defense")
print(S.iloc[:, [0, 6]])

# Total
S = df.nsmallest(5, "Sp_Atk")
print(S.iloc[:, [0, 7]])

# Total
S = df.nsmallest(5, "Sp_Def")
print(S.iloc[:, [0, 8]])

# Total
S = df.nsmallest(5, "Speed")
print(S.iloc[:, [0, 9]])

#####

# How many legendaries and who are they?

Leg = df["isLegendary"] == True

Gen1 = df["Generation"] == 1
Gen2 = df["Generation"] == 2
Gen3 = df["Generation"] == 3
Gen4 = df["Generation"] == 4
Gen5 = df["Generation"] == 5
Gen6 = df["Generation"] == 6

Gen1Legendary = df.loc[np.logical_and(Gen1, Leg)]
Gen2Legendary = df.loc[np.logical_and(Gen2, Leg)]
Gen3Legendary = df.loc[np.logical_and(Gen3, Leg)]
Gen4Legendary = df.loc[np.logical_and(Gen4, Leg)]
Gen5Legendary = df.loc[np.logical_and(Gen5, Leg)]
Gen6Legendary = df.loc[np.logical_and(Gen6, Leg)]

print("\n", "There are a total of:", len(df.loc[Leg]), "legendary Pokémon")

print(Gen1Legendary["Name"])
print(Gen2Legendary["Name"])
print(Gen3Legendary["Name"])
print(Gen4Legendary["Name"])
print(Gen5Legendary["Name"])
print(Gen6Legendary["Name"])

# Exceptions to the legendary trend
Sub600 = df["Total"] < 600
Gendered = df["hasGender"] == True
EggGroup = df["Egg_Group_1"] != "Undiscovered"

LegendarySub600 = df.loc[np.logical_and(Sub600, Leg)]
LegendaryGendered = df.loc[np.logical_and(Gendered, Leg)]
LegendaryEggGroup = df.loc[np.logical_and(EggGroup, Leg)]

print("For sub-600 total exceptions, we have:")
print(LegendarySub600[["Name", "Total"]])
print("\n")
print("For gendered exceptions, we have:")
print(LegendaryGendered[["Name", "hasGender", "Pr_Male"]])
print("\n")
print("For egg group exceptions, we have:")
print(LegendaryEggGroup[["Name"]])

#####

#Who has Gender?
Gender = UniqueWordCounter("PokemonData.csv" ,"hasGender")
PrMale = UniqueWordCounter("PokemonData.csv" ,"Pr_Male")

Gender_Key, Gender_Val = ListGenerator(Gender)
PrMale_Key, PrMale_Val = ListGenerator(PrMale)