"""
This script was designed to bring everything together, to be run during the presentation in order to demonstrate all of
the insights of the data and the facets of the pipeline I developed.
"""

"""
# Importing the relevent libraries as their usual aliases
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Setting the random number for repeatability
np.random.seed(42)

"""
# Generating the DataFrames from the edited local files
"""

# Accidents
df_Acc_2016 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2016", index_col="Accident_Index")
df_Acc_2015 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2015", index_col="Accident_Index")
df_Acc_2014 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2014", index_col="Accident_Index")
df_Acc_2013 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2013", index_col="Accident_Index")
df_Acc_2012 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2012", index_col="Accident_Index")
df_Acc_2011 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2011", index_col="Accident_Index")
df_Acc_2010 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2010", index_col="Accident_Index")
df_Acc_2009 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2009", index_col="Accident_Index")

# Casualties
df_Cas_2016 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2016", index_col="Accident_Index")
df_Cas_2015 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2015", index_col="Accident_Index")
df_Cas_2014 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2014", index_col="Accident_Index")
df_Cas_2013 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2013", index_col="Acc_Index")
df_Cas_2012 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2012", index_col="Acc_Index")
df_Cas_2011 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2011", index_col="Acc_Index")
df_Cas_2010 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2010", index_col="Acc_Index")
df_Cas_2009 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2009", index_col="Acc_Index")

# Vehicles
df_Veh_2016 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2016", index_col="Accident_Index")
df_Veh_2015 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2015", index_col="Accident_Index")
df_Veh_2014 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2014", index_col="Accident_Index")
df_Veh_2013 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2013", index_col="Acc_Index")
df_Veh_2012 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2012", index_col="Acc_Index")
df_Veh_2011 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2011", index_col="Acc_Index")
df_Veh_2010 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2010", index_col="Acc_Index")
df_Veh_2009 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2009", index_col="Acc_Index")

"""
# XXXxxxXXX
"""