"""
The purpose of this script is to test importing and building the DataFrames 1) by downloading the files from the website
directly and 2) by pointing to the files saved locally for offline work / the presentation.
"""

"""
# Preamble
"""
# Import the relevant libraries with their usual aliases
from urllib.request import urlopen
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Setting the random number for repeatability
np.random.seed(42)

"""
# Setting up useful functions
"""

def DataFrameGeneration(url):

    """ Given a url, download the .zip file, generate the DataFrame, and delete the locally stored .zip"""

    # open and save the zip file onto computer
    URL = urlopen(url)
    output = open('Temp.zip', 'wb')
    output.write(URL.read())
    output.close()

    # read the zip file as a pandas dataframe
    df = pd.read_csv('Temp.zip')  # pandas version 0.18.1 takes zip files

    # if keeping on disk the zip file is not wanted, then:
    os.remove('Temp.zip')  # remove the copy of the zipfile on disk

    return df

"""
# Defining the urls of the data on the government website:
# https://data.gov.uk/dataset/road-accidents-safety-data
"""

# Define the urls of the zipped data files

# 2016
url_2016_MakeAndModel = "http://data.dft.gov.uk/road-accidents-safety-data/MakeModel2016.zip"
url_2016_Casualties = "http://data.dft.gov.uk/road-accidents-safety-data/dftRoadSafetyData_Casualties_2016.zip"
url_2016_Vehicles = "http://data.dft.gov.uk/road-accidents-safety-data/dftRoadSafetyData_Vehicles_2016.zip"
url_2016_Accidents = "http://data.dft.gov.uk/road-accidents-safety-data/dftRoadSafety_Accidents_2016.zip"

# 2015
url_2015_MakeAndModel = "http://data.dft.gov.uk.s3.amazonaws.com/road-accidents-safety-data/MakeModel2015.zip"
url_2015_CasualtyDashboard = "http://data.dft.gov.uk/road-accidents-safety-data/DfTCasualtyDashboard.zip"
url_2015_AllRoadSafetyData = "http://data.dft.gov.uk/road-accidents-safety-data/RoadSafetyData_2015.zip"
url_2015_Casualties = "http://data.dft.gov.uk/road-accidents-safety-data/RoadSafetyData_Casualties_2015.zip"
url_2015_Vehicles = "http://data.dft.gov.uk/road-accidents-safety-data/RoadSafetyData_Vehicles_2015.zip"
url_2015_Accidents = "http://data.dft.gov.uk/road-accidents-safety-data/RoadSafetyData_Accidents_2015.zip"

# 2014
url_2014_MakeAndModel = "http://data.dft.gov.uk.s3.amazonaws.com/road-accidents-safety-data/Road%20Safety%20-%20Vehicles%20by%20Make%20and%20Model%202014.zip"
url_2014_BreathTest = "http://data.dft.gov.uk/road-accidents-safety-data/DigitalBreathTestData2014.zip"
url_2005to2014_AccidentCasualtiesVehicle = "http://data.dft.gov.uk.s3.amazonaws.com/road-accidents-safety-data/Stats19_Data_2005-2014.zip" # 3 in 1
url_2014_Casualties = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Casualties_2014.zip"
url_2014_Vehicles = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Vehicles_2014.zip"
url_2014_Accidents = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Accidents_2014.zip"

# 2013
url_2013_MakeAndModel = "http://data.dft.gov.uk/road-accidents-safety-data/Road%20Safety%20-%20Vehicles%20by%20Make%20and%20Model%202013.zip"
url_2013_BreathTest = "http://data.dft.gov.uk/road-accidents-safety-data/DigitalBreathTestData2013.zip"
url_2013_BloodAlcoholMatchedCoronersData = "http://data.dft.gov.uk/road-accidents-safety-data/BloodAlcoholContent-CoronersMatchedData2013.zip"
url_2013_Casualties = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Casualties_2013.zip"
url_2013_Vehicles = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Vehicles_2013.zip"
url_2013_Accidents = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Accidents_2013.zip"

# 2012
url_2012_MakeAndModel = "http://data.dft.gov.uk/road-accidents-safety-data/STATS19VehicleAccidentData2012MakeModel.zip"
url_2012_BreathTest = "http://data.dft.gov.uk/road-accidents-safety-data/DigitalBreathTestData2012.zip"
url_2012_BloodAlcoholMatchedCoronersData = "http://data.dft.gov.uk/road-accidents-safety-data/BloodAlcoholContent-CoronersMatchedData2012.zip"
url_2012_Casualties = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Casualties_2012.zip"
url_2012_Vehicles = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Vehicles_2012.zip"
url_2012_Accidents = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Accidents_2012.zip"

# 2011
url_2011_MakeAndModel = "http://data.dft.gov.uk/road-accidents-safety-data/STATS19VehicleAccidentData2011MakeModel.zip"
url_2011_BreathTest = "http://data.dft.gov.uk/road-accidents-safety-data/DigitalBreathTestData2011.zip"
url_2011_BloodAlcoholMatchedCoronersData = "http://data.dft.gov.uk/road-accidents-safety-data/BloodAlcoholContent-CoronersMatchedData2011.zip"
url_2011_Casualties = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Casualties_2011.zip"
url_2011_Vehicles = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Vehicles_2011.zip"
url_2011_Accidents = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Accidents_2011.zip"

# 2010
url_2010_MakeAndModel = "http://data.dft.gov.uk/road-accidents-safety-data/STATS19VehicleAccidentData2010MakeModel.zip"
url_2010_BreathTest = "http://data.dft.gov.uk/road-accidents-safety-data/DigitalBreathTestData2010.zip"
url_2010_BloodAlcoholMatchedCoronersData = "http://data.dft.gov.uk/road-accidents-safety-data/BloodAlcoholContent-CoronersMatchedData2010.zip"
url_2010_Casualties = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Casualties_2010.zip"
url_2010_Vehicles = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Vehicles_2010.zip"
url_2010_Accidents = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Accidents_2010.zip"

# 2009
url_2009_MakeAndModel = "http://data.dft.gov.uk/road-accidents-safety-data/STATS19VehicleAccidentData2009MakeModel.zip"
url_2009_BreathTest = "http://data.dft.gov.uk/road-accidents-safety-data/DigitalBreathTestData2009.zip"
url_2009_BloodAlcoholMatchedCoronersData = "http://data.dft.gov.uk/road-accidents-safety-data/BloodAlcoholContent-CoronersMatchedData2009.zip"
url_2009_Casualties = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Casualties_2009.zip"
url_2009_Vehicles = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Vehicles_2009.zip"
url_2009_Accidents = "http://data.dft.gov.uk/road-accidents-safety-data/DfTRoadSafety_Accidents_2009.zip"

"""
# Defining the paths to local documents in order to work offline
"""

# 2016

path_Accidents_2016 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Accidents_2016.csv"
path_Casualties_2016 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Casualties_2016.csv"
path_Vehicles_2016 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Vehicles_2016.csv"

# 2015

path_Accidents_2015 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Accidents_2015.csv"
path_Casualties_2015 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Casualties_2015.csv"
path_Vehicles_2015 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Vehicles_2015.csv"

# 2014

path_Accidents_2014 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Accidents_2014.csv"
path_Casualties_2014 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Casualties_2014.csv"
path_Vehicles_2014 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Vehicles_2014.csv"

# 2013

path_Accidents_2013 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Accidents_2013.csv"
path_Casualties_2013 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Casualties_2013.csv"
path_Vehicles_2013 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Vehicles_2013.csv"

# 2012

path_Accidents_2012 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Accidents_2012.csv"
path_Casualties_2012 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Casualties_2012.csv"
path_Vehicles_2012 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Vehicles_2012.csv"

# 2011

path_Accidents_2011 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Accidents_2011.csv"
path_Casualties_2011 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Casualties_2011.csv"
path_Vehicles_2011 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Vehicles_2011.csv"

# 2010

path_Accidents_2010 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Accidents_2010.csv"
path_Casualties_2010 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Casualties_2010.csv"
path_Vehicles_2010 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Vehicles_2010.csv"

# 2009

path_Accidents_2009 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Accidents_2009.csv"
path_Casualties_2009 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Casualties_2009.csv"
path_Vehicles_2009 = r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\DataFiles\DfTRoadSafety_Vehicles_2009.csv"

"""
# Defining the lists of urls
"""

urlList_Accidents_2016to2009 = [url_2016_Accidents, url_2015_Accidents, url_2014_Accidents, url_2013_Accidents, url_2012_Accidents, url_2011_Accidents, url_2010_Accidents, url_2009_Accidents]
urlList_Casualties_2016to2009 = [url_2016_Casualties, url_2015_Casualties, url_2014_Casualties, url_2013_Casualties, url_2012_Casualties, url_2011_Casualties, url_2010_Casualties, url_2009_Casualties]
urlList_Vehicles_2016to2009 = [url_2016_Vehicles, url_2015_Vehicles, url_2014_Vehicles, url_2013_Vehicles, url_2012_Vehicles, url_2011_Vehicles, url_2010_Vehicles, url_2009_Vehicles]

urlList_Accidents_2016to2012 = [url_2016_Accidents, url_2015_Accidents, url_2014_Accidents, url_2013_Accidents, url_2012_Accidents]
urlList_Casualties_2016to2012 = [url_2016_Casualties, url_2015_Casualties, url_2014_Casualties, url_2013_Casualties, url_2012_Casualties]
urlList_Vehicles_2016to2012 = [url_2016_Vehicles, url_2015_Vehicles, url_2014_Vehicles, url_2013_Vehicles, url_2012_Vehicles]

"""
# Generating the DataFrames from the local files
"""

# Accidents
df_Acc_2016 = pd.read_csv(path_Accidents_2016, index_col="Accident_Index")
df_Acc_2015 = pd.read_csv(path_Accidents_2015, index_col="Accident_Index")
df_Acc_2014 = pd.read_csv(path_Accidents_2014, index_col="Accident_Index")
df_Acc_2013 = pd.read_csv(path_Accidents_2013, index_col="Accident_Index")
df_Acc_2012 = pd.read_csv(path_Accidents_2012, index_col="Accident_Index")
df_Acc_2011 = pd.read_csv(path_Accidents_2011, index_col="Accident_Index")
df_Acc_2010 = pd.read_csv(path_Accidents_2010, index_col="Accident_Index")
df_Acc_2009 = pd.read_csv(path_Accidents_2009, index_col="Accident_Index")

# Casualties
df_Cas_2016 = pd.read_csv(path_Casualties_2016, index_col="Accident_Index")
df_Cas_2015 = pd.read_csv(path_Casualties_2015, index_col="Accident_Index")
df_Cas_2014 = pd.read_csv(path_Casualties_2014, index_col="Accident_Index")
df_Cas_2013 = pd.read_csv(path_Casualties_2013, index_col="Acc_Index")
df_Cas_2012 = pd.read_csv(path_Casualties_2012, index_col="Acc_Index")
df_Cas_2011 = pd.read_csv(path_Casualties_2011, index_col="Acc_Index")
df_Cas_2010 = pd.read_csv(path_Casualties_2010, index_col="Acc_Index")
df_Cas_2009 = pd.read_csv(path_Casualties_2009, index_col="Acc_Index")

# Vehicles
df_Veh_2016 = pd.read_csv(path_Vehicles_2016, index_col="Accident_Index")
df_Veh_2015 = pd.read_csv(path_Vehicles_2015, index_col="Accident_Index")
df_Veh_2014 = pd.read_csv(path_Vehicles_2014, index_col="Accident_Index")
df_Veh_2013 = pd.read_csv(path_Vehicles_2013, index_col="Acc_Index")
df_Veh_2012 = pd.read_csv(path_Vehicles_2012, index_col="Acc_Index")
df_Veh_2011 = pd.read_csv(path_Vehicles_2011, index_col="Acc_Index")
df_Veh_2010 = pd.read_csv(path_Vehicles_2010, index_col="Acc_Index")
df_Veh_2009 = pd.read_csv(path_Vehicles_2009, index_col="Acc_Index")
