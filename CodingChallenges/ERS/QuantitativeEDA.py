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
# Initial examination
"""

# Extract the column names:
colNamesAll = list(df)

# Print the headers
for item in colNamesAll:
    print(df[str(item)].head(10))

# Print the information
print(df.info())

# Describe the columns with summary statistics
for item in colNamesAll:
    print(df[str(item)].describe())
    print("\n")

# Looking at the number of categories in the Location Type column
print("The number of unique objects in total is:", df["Location_Type"].nunique())
print("\n")
print("They can be counted as follows:")
print("\n")
print(pd.crosstab(index=df["Location_Type"], columns="count"))

# Searching for the Inf values
#print(df.loc[df.Points_Per_License == "Inf"])

# Searching for the high frequency value(s)
#print(df.loc[df.Frequency >= 1.0])

"""
# Plotting the correlation matrix
"""

# Set the style
sns.set(style="white")

# Compute the correlation matrix
corr = df.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.show()