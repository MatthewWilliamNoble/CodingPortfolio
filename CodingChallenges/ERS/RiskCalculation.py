# Import the relevant libraries with their usual aliases
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set the random number for reproducibility
np.random.seed(42)

# Set the plotting style to Seaborn
sns.set()

"""
# Data import
"""

# Importing the data
df = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\ERS\ERS_Technical_Assessment_data.csv", index_col="Region")

"""
# Creating the relevant summary statistics for risk calculation
"""

# Extract the column names:
colNamesAll = list(df)

# Defining the Number of claims per region
df["Number_Of_Claims_Per_Region"] = df["Frequency"] * df["Exposure (EVY)"]

# Defining the number of claims per region per driver
df["Number_Of_Claims_Per_Region_Per_Driver"] = df["Number_Of_Claims_Per_Region"] / df["Avg_Drivers"]

# Defining the number of incidents per driver
df["Total_Local_Incidents"] = df["Local_Incidents_Sev1"] + df["Local_Incidents_Sev2"] + df["Local_Incidents_Sev3"]
df["Total_Local_Incidents_Per_Driver"] = df["Total_Local_Incidents"] / df["Avg_Drivers"]

"""
# Performing linear interpolation on the data to scale it between 1 and 99 relative to other region values
"""

# Building the backbone functions

def LinearInterpolationINTEGER(Value, OldMin, OldMax, NewMin, NewMax):
    """ Function to scale a value between one range to a new value between a new range """
    return int((Value - OldMin) * ((NewMax - NewMin) / (OldMax - OldMin)) + (NewMin))

def Scaler(DataFrame, Column, NewColumn):

    """ Function to apply the LinearInterpolationINTEGER function to a column of a DataFrame and append the answer as
     a new column """

    ListToAdd = []
    MIN = min(DataFrame[Column])
    MAX = max(DataFrame[Column])

    for index, row in DataFrame.iterrows():
        ListToAdd.append(LinearInterpolationINTEGER(row[Column], MIN, MAX, 1, 99))

    DataFrame[NewColumn] = ListToAdd

# Implementing it to the relevant fields

Scaler(df, "Frequency", "Frequency_Scaled")
Scaler(df, "Non_Area_Related_Veh_Risk", "Non_Area_Related_Veh_Risk_Scaled")
Scaler(df, "Number_Of_Claims_Per_Region_Per_Driver", "Number_Of_Claims_Per_Region_Per_Driver_Scaled")
Scaler(df, "Total_Local_Incidents_Per_Driver", "Total_Local_Incidents_Per_Driver_Scaled")
Scaler(df, "Traffic_Flow", "Traffic_Flow_Scaled")
Scaler(df, "Points_Per_License_Avg", "Points_Per_License_Avg_Scaled")

"""
# Defining the actual risk score
"""

df["RiskScore_SUM"] = (df["Frequency_Scaled"] +
                       df["Non_Area_Related_Veh_Risk_Scaled"]+
                       df["Number_Of_Claims_Per_Region_Per_Driver_Scaled"]+
                       df["Total_Local_Incidents_Per_Driver_Scaled"]+
                       df["Traffic_Flow_Scaled"]+
                       df["Points_Per_License_Avg_Scaled"]
                       )

# Rescaling to give a final risk score

Scaler(df, "RiskScore_SUM", "RiskScore_SUM_Scaled")

"""
# Plotting the distribution of the final results
"""

_ = sns.distplot(df["RiskScore_SUM_Scaled"], bins=99, norm_hist=True)
_ = plt.xlabel("Relative Risk Score")
_ = plt.ylabel("Frequency")
_ = plt.title("Normalised Histogram Detailing the Distribution of Relative Risk Scores for Each Region")
_ = plt.margins(0.02)

plt.show()

"""
# Printing the relative risk as a .csv
"""

# Renaming the field
df["Score"] = df["RiskScore_SUM_Scaled"]

# Saving the .csv
df.to_csv(path_or_buf=r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\ERS\TechnicalAssessmentERS_Submission_M_W_Noble.csv", index_label="Region" ,columns=["Score"])