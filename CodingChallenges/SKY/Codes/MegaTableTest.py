"""
A brief script to merge all of the 3 tables over the 5 years into one mega table
"""

import pandas as pd
import numpy as np

"""
# Merging the all files into one final DataFrame
"""

Temp2016 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\All_Of_2016", index_col="Accident_Index")

Temp2015 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\All_Of_2015", index_col="Accident_Index")

Temp2014 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\All_Of_2014", index_col="Accident_Index")

Temp2013 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\All_Of_2013", index_col="Unnamed: 0")
Temp2013.index.names = ['Accident_Index']

Temp2012 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\All_Of_2012", index_col="Unnamed: 0")
Temp2012.index.names = ['Accident_Index']

MegaTable = pd.concat([Temp2016, Temp2015, Temp2014, Temp2013, Temp2012], axis=0)

MegaTable.to_csv("MegaTable_2016to2012", sep=",", index=True)

print(MegaTable.info())


