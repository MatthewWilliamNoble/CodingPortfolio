"""
The purpose of this script is to design the plotting pipeline.
"""

"""
# Importing the relevent libraries as their usual aliases
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.style.use('ggplot')

# Setting the random number for repeatability
np.random.seed(42)

"""
# Generating the DataFrames from the edited local files
"""

# Accidents
#df_Acc_2016 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2016", index_col="Accident_Index")
#df_Acc_2015 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2015", index_col="Accident_Index")
#df_Acc_2014 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2014", index_col="Accident_Index")
#df_Acc_2013 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2013", index_col="Accident_Index")
#df_Acc_2012 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2012", index_col="Accident_Index")
#df_Acc_2011 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2011", index_col="Accident_Index")
#df_Acc_2010 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2010", index_col="Accident_Index")
#df_Acc_2009 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Accidents_2009", index_col="Accident_Index")

# Casualties
#df_Cas_2016 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2016", index_col="Accident_Index")
#df_Cas_2015 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2015", index_col="Accident_Index")
#df_Cas_2014 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2014", index_col="Accident_Index")
#df_Cas_2013 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2013", index_col="Acc_Index")
#df_Cas_2012 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2012", index_col="Acc_Index")
#df_Cas_2011 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2011", index_col="Acc_Index")
#df_Cas_2010 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2010", index_col="Acc_Index")
#df_Cas_2009 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Casualties_2009", index_col="Acc_Index")

# Vehicles
#df_Veh_2016 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2016", index_col="Accident_Index")
#df_Veh_2015 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2015", index_col="Accident_Index")
#df_Veh_2014 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2014", index_col="Accident_Index")
#df_Veh_2013 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2013", index_col="Acc_Index")
#df_Veh_2012 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2012", index_col="Acc_Index")
#df_Veh_2011 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2011", index_col="Acc_Index")
#df_Veh_2010 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2010", index_col="Acc_Index")
#df_Veh_2009 = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\Vehicle_2009", index_col="Acc_Index")

# Creating lists of the DataFrames
#list_Acc = [df_Acc_2016, df_Acc_2015, df_Acc_2014, df_Acc_2013, df_Acc_2012, df_Acc_2011, df_Acc_2010, df_Acc_2009]
#list_Cas = [df_Cas_2016, df_Cas_2015, df_Cas_2014,df_Cas_2013, df_Cas_2012, df_Cas_2011,df_Cas_2010,df_Cas_2009]
#list_Veh = [df_Veh_2016, df_Veh_2015, df_Veh_2014, df_Veh_2013, df_Veh_2012, df_Veh_2011, df_Veh_2010, df_Veh_2009]

# Importing the MegaTable

#MegaTable = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\MegaTable_2016to2012", index_col="Accident_Index")

"""
# Combining the DataFrames and pivoting around the AccidentIndex
"""

# Merging the DataFrames on the unique index

# All 2016
'''
Temp = pd.merge(df_Acc_2016, df_Veh_2016, left_index=True, right_index=True, how="outer")
All_Of_2016 = pd.merge(Temp, df_Cas_2016, left_index=True, right_index=True, how="outer")
All_Of_2016["Collection_Year"] = 2016

# All 2015

Temp = pd.merge(df_Acc_2015, df_Veh_2015, left_index=True, right_index=True, how="outer")
All_Of_2015 = pd.merge(Temp, df_Cas_2015, left_index=True, right_index=True, how="outer")
All_Of_2015["Collection_Year"] = 2015

# All 2014

Temp = pd.merge(df_Acc_2014, df_Veh_2014, left_index=True, right_index=True, how="outer")
All_Of_2014 = pd.merge(Temp, df_Cas_2014, left_index=True, right_index=True, how="outer")
All_Of_2014["Collection_Year"] = 2014

# All 2013

Temp = pd.merge(df_Acc_2013, df_Veh_2013, left_index=True, right_index=True, how="outer")
All_Of_2013 = pd.merge(Temp, df_Cas_2013, left_index=True, right_index=True, how="outer")
All_Of_2013["Collection_Year"] = 2013

# All 2012

Temp = pd.merge(df_Acc_2012, df_Veh_2012, left_index=True, right_index=True, how="outer")
All_Of_2012 = pd.merge(Temp, df_Cas_2012, left_index=True, right_index=True, how="outer")
All_Of_2012["Collection_Year"] = 2012

# All 2011

Temp = pd.merge(df_Acc_2011, df_Veh_2011, left_index=True, right_index=True, how="outer")
All_Of_2011 = pd.merge(Temp, df_Cas_2011, left_index=True, right_index=True, how="outer")
All_Of_2011["Collection_Year"] = 2011

# All 2010

Temp = pd.merge(df_Acc_2010, df_Veh_2010, left_index=True, right_index=True, how="outer")
All_Of_2010 = pd.merge(Temp, df_Cas_2010, left_index=True, right_index=True, how="outer")
All_Of_2010["Collection_Year"] = 2010

# All 2009

Temp = pd.merge(df_Acc_2009, df_Veh_2009, left_index=True, right_index=True, how="outer")
All_Of_2009 = pd.merge(Temp, df_Cas_2009, left_index=True, right_index=True, how="outer")
All_Of_2009["Collection_Year"] = 2009
'''

"""
# Numerical investigations
    # Column Headings
    # Describing the numerical data
    # Generate a crosstab to show counts
"""

"""
# Column Headings
"""

#for element in list_Acc:
#    print(list(element))

# Describe each column within a DataFrame

#for item in list_Acc:
#
#    print("\n")
#    print(item.describe())
#    print("\n")
#
#for item in list_Cas:
#
#    print("\n")
#    print(item.describe())
#    print("\n")
#
#for item in list_Veh:
#
#    print("\n")
#    print(item.describe())
#    print("\n")

# Print all of the DataFrames columns

#for item in list(df_Acc_2016):
#    print(item)

# Generate a CrossTab of the DataFrame. This will return the count of each object within the categorical column.

#print(pd.crosstab(index=df_Veh_2016["Journey_Purpose_of_Driver"], columns="count"))

# Generae new DataFrames based on queries. Logical AND, logical OR, or even filtering

#New = df_Veh_2016.loc[np.logical_and((df_Veh_2016["Journey_Purpose_of_Driver"] == "Journey as part of work"), (df_Veh_2016["Sex_of_Driver"]=="Male"))]
#print(New.info())

#New = df_Veh_2016.loc[df_Veh_2016["Sex_of_Driver"]=="Male"]
#print(New.info())

#New = df_Acc_2016.loc[df_Acc_2016["Speed_limit"]<=30]
#print(New.info())

"""
# Univariate Plotting
    # Count Plots as Percentage Vs. Category
"""

"""
# Count Plot as Percentage Vs. Category
"""
"""
# Define the DataFrame
df = df_Veh_2016
ncount = len(df)

plt.figure(figsize=(12,8))
ax = sns.countplot(x='1st_Point_of_Impact', data=df_Veh_2016)
plt.title('XXXXX')
plt.xlabel('XXXXX')
#plt.xticks(rotation=45)

# Make twin axis
ax2=ax.twinx()

# Switch so count axis is on right, frequency on left
ax2.yaxis.tick_left()
ax.yaxis.tick_right()

# Also switch the labels over
ax.yaxis.set_label_position('right')
ax2.yaxis.set_label_position('left')

# Name the y-axes
ax2.set_ylabel('Frequency [%]')
ax.set_ylabel('Absolute Count')

for p in ax.patches:
    x=p.get_bbox().get_points()[:,0]
    y=p.get_bbox().get_points()[1,1]
    ax.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y),
            ha='center', va='bottom') # set the alignment of the text

# Use a LinearLocator to ensure the correct number of ticks
ax.yaxis.set_major_locator(ticker.LinearLocator(11))

# Fix the frequency range to 0-100
ax2.set_ylim(0,100)
ax.set_ylim(0,ncount)

# And use a MultipleLocator to ensure a tick spacing of 10
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))

# Need to turn the grid on ax2 off, otherwise the gridlines end up on top of the bars
ax2.grid(None)

plt.show()
"""
"""
# Bivariate Plotting
    # CountPlot separated by category
"""

"""
# CountPlot separated by category (in this case year)
"""

# Editing mistakes as I find them
#LU = {"-1":"Data missing or out of range"}
#MegaTable["2nd_Road_Class"].replace(LU, inplace=True)
#MegaTable.to_csv("MegaTable_2016to2012", sep=",", index=True)

# Forced to hard code order for appearance

#sns.countplot(x=MegaTable["Age_Band_of_Driver"], hue=MegaTable["Collection_Year"], order=["0 - 5", "6 - 10", "11 - 15", "16 - 20", "21 - 25", "26 - 35", "36 - 45", "46 - 55", "56 - 65", "66 - 75", "Over 75", "Data missing or out of range"])
#plt.ylabel("Count")
#plt.title("Count-Plot showing Age_Band_of_Driver by Year")
#plt.xticks(rotation="vertical")
#plt.show()

#sns.countplot(x=MegaTable["Driver_IMD_Decile"], hue=MegaTable["Collection_Year"], order=["Most deprived 10%", "More deprived 10-20%", "More deprived 20-30%", "More deprived 30-40%","More deprived 40-50%","Less deprived 40-50%","Less deprived 30-40%","Less deprived 20-30%","Less deprived 10-20%","Least deprived 10%","Data missing or out of range"])
#plt.ylabel("Count")
#plt.title("Count-Plot showing Driver_IMD_Decile by Year")
#plt.xticks(rotation="vertical")
#plt.show()

#sns.countplot(x=MegaTable["Day_of_Week"], hue=MegaTable["Collection_Year"], order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
#plt.ylabel("Count")
#plt.title("Count-Plot showing Day_of_Week by Year")
#plt.xticks(rotation="vertical")
#plt.show()

#sns.countplot(x=MegaTable["Vehicle_Leaving_Carriageway"], hue=MegaTable["Collection_Year"])
#plt.ylabel("Count")
#plt.title("Count-Plot showing Vehicle_Leaving_Carriageway by Year")
#plt.xticks(rotation="vertical")
#plt.show()

"""
# Trivariate Plotting
    # CountPlot separated by category and columned by category 
"""

"""
# CountPlot separated by category and columned by category
"""

# Plotting two fields via year in column

#g = sns.factorplot(x="NumOfCas_Banded", hue="Age_Band_of_Driver", col="Year", data=MegaTable, kind="count", order=["1", "2", "3", "4", "5", "6 - 10", "11 - 20", "21+"], hue_order=["0 - 5", "6 - 10", "11 - 15", "16 - 20", "21 - 25", "26 - 35", "36 - 45", "46 - 55", "56 - 65", "66 - 75", "Over 75", "Data missing or out of range"], legend=False)
#g = sns.factorplot(x="NumOfCas_Banded", hue="Vehicle_IMD_Decile", col="Year", data=MegaTable, kind="count", order=["1", "2", "3", "4", "5", "6 - 10", "11 - 20", "21+"], hue_order=["Most deprived 10%", "More deprived 10-20%", "More deprived 20-30%", "More deprived 30-40%","More deprived 40-50%","Less deprived 40-50%","Less deprived 30-40%","Less deprived 20-30%","Less deprived 10-20%","Least deprived 10%","Data missing or out of range"], legend=False)
#g = sns.factorplot(x="NumOfCas_Banded", hue="Day_of_Week", col="Year", data=MegaTable, kind="count", order=["1", "2", "3", "4", "5", "6 - 10", "11 - 20", "21+"], hue_order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], legend=False)

#g = sns.factorplot(x="NumOfCas_Banded", hue="1st_Point_of_Impact", col="Year", data=MegaTable, kind="count", order=["1", "2", "3", "4", "5", "6 - 10", "11 - 20", "21+"], legend=False)

# Only 2016 Data ... Repeating

MegaTable = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\MegaTable_2016", index_col="Accident_Index")

#g = sns.factorplot(x="NumOfCas_Banded", hue="1st_Road_Class", data=MegaTable, kind="count", order=["1", "2", "3", "4", "5", "6 - 10", "11 - 20", "21+"], hue_order=["A", "B", "C", "A(M)", "Motorway", "Unclassified"], legend=False)
#g = sns.factorplot(x="NumOfCas_Banded", hue="Age_Band_of_Driver", data=MegaTable, kind="count", order=["1", "2", "3", "4", "5", "6 - 10", "11 - 20", "21+"], hue_order=["0 - 5", "6 - 10", "11 - 15", "16 - 20", "21 - 25", "26 - 35", "36 - 45", "46 - 55", "56 - 65", "66 - 75", "Over 75", "Data missing or out of range"], legend=False)
#g = sns.factorplot(x="NumOfCas_Banded", hue="Vehicle_IMD_Decile",data=MegaTable, kind="count", order=["1", "2", "3", "4", "5", "6 - 10", "11 - 20", "21+"], hue_order=["Most deprived 10%", "More deprived 10-20%", "More deprived 20-30%", "More deprived 30-40%","More deprived 40-50%","Less deprived 40-50%","Less deprived 30-40%","Less deprived 20-30%","Less deprived 10-20%","Least deprived 10%","Data missing or out of range"], legend=False)
#g = sns.factorplot(x="NumOfCas_Banded", hue="Day_of_Week", data=MegaTable, kind="count", order=["1", "2", "3", "4", "5", "6 - 10", "11 - 20", "21+"], hue_order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], legend=False)

#g = sns.factorplot(x="NumOfCas_Banded", hue="Weather_Conditions", data=MegaTable, kind="count", order=["1", "2", "3", "4", "5", "6 - 10", "11 - 20", "21+"], legend=False)

#g.set_xticklabels(rotation=45)
#g.set_xlabels("Number of Casualties")
#plt.legend(loc=1)
#plt.show()

#for item in list(MegaTable):
#    print(MegaTable[str(item)].head())

print(MegaTable.info())

print(MegaTable.Date.head())

