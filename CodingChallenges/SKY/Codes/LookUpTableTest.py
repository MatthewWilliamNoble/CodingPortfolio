"""
The purpose of this script is to build on the ImportingTest.py script and combine the DataFrames with look-up tables sup
plied in the additional documents folder to change the information from cryptic numbers to actual words..
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

"""
# Defining look-up tables as dictionaries given the accompanying .xlsx file
"""

LU_Police_Force = {1:"Metropolitan Police", 3:"Cumbria", 4:"Lancashire", 5:"Merseyside", 6:"Greater Manchester",
                   7:"Cheshire", 10:"Northumbria", 11:"Durham", 12:"North Yorkshire", 13:"West Yorkshire",
                   14:"South Yorkshire", 16:"Humberside", 17:"Cleveland", 20:"West Midlands", 21:"Staffordshire",
                   22:"West Mercia", 23:"Warwickshire", 30:"Derbyshire", 31:"Nottinghamshire", 32:"Lincolnshire",
                   33:"Leicestershire", 34:"Northamptonshire", 35:"Cambridgeshire", 36:"Norfolk", 37:"Suffolk",
                   40:"Bedfordshire", 41:"Hertfordshire", 42:"Essex", 43:"Thames Valley", 44:"Hampshire", 45:"Surrey",
                   46:"Kent", 47:"Sussex", 48:"City of London", 50:"Devon and Cornwall", 52:"Avon and Somerset",
                   53:"Gloucestershire", 54:"Wiltshire", 55:"Dorset", 60:"North Wales", 61:"Gwent", 62:"South Wales",
                   63:"Dyfed-Powys", 91:"Northern", 92:"Grampian", 93:"Tayside", 94:"Fife", 95:"Lothian and Borders",
                   96:"Central", 97:"Strathclyde", 98:"Dumfries and Galloway"}

LU_Accident_Severity = {1:"Fatal", 2:"Serious", 3:"Slight"}

LU_Day_of_Week = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}

LU_Local_Authority_District = {1:"Westminster", 2:"Camden", 3:"Islington", 4:"Hackney", 5:"Tower Hamlets", 6:"Greenwich", 7:"Lewisham", 8:"Southwark",
                               9:"Lambeth", 10:"Wandsworth", 11:"Hammersmith and Fulham", 12:"Kensington and Chelsea", 13:"Waltham Forest", 14:"Redbridge", 15:"Havering", 16:"Barking and Dagenham",
                               17:"Newham", 18:"Bexley", 19:"Bromley", 20:"Croydon", 21:"Sutton", 22:"Merton", 23:"Kingston upon Thames", 24:"Richmond upon Thames",
                               25:"Hounslow", 26:"Hillingdon", 27:"Ealing", 28:"Brent", 29:"Harrow", 30:"Barnet", 31:"Haringey", 32:"Enfield",
                               33:"Hertsmere", 38:"Epsom and Ewell", 40:"Spelthorne", 57:"London Airport (Heathrow)", 60:"Allerdale", 61:"Barrow-in-Furness", 62:"Carlisle", 63:"Copeland",
                               64:"Eden", 65:"South Lakeland", 70:"Blackburn with Darwen", 71:"Blackpool", 72:"Burnley", 73:"Chorley", 74:"Fylde", 75:"Hyndburn",
                               76:"Lancaster", 77:"Pendle", 79:"Preston", 80:"Ribble Valley", 82:"Rossendale", 83:"South Ribble", 84:"West Lancashire", 85:"Wyre",
                               90:"Knowsley", 91:"Liverpool", 92:"St. Helens", 93:"Sefton", 95:"Wirral", 100:"Bolton", 101:"Bury", 102:"Manchester",
                               104:"Oldham", 106:"Rochdale", 107:"Salford", 109:"Stockport", 110:"Tameside", 112:"Trafford", 114:"Wigan", 120:"Chester",
                               121:"Congleton", 122:"Crewe and Nantwich", 123:"Ellesmere Port and Neston", 124:"Halton", 126:"Macclesfield", 127:"Vale Royal", 128:"Warrington", 129:"Cheshire East",
                               130:"Cheshire West and Chester", 139:"Northumberland", 140:"Alnwick", 141:"Berwick-upon-Tweed", 142:"Blyth Valley", 143:"Castle Morpeth", 144:"Tynedale", 145:"Wansbeck",
                               146:"Gateshead", 147:"Newcastle upon Tyne", 148:"North Tyneside", 149:"South Tyneside", 150:"Sunderland", 160:"Chester-le-Street", 161:"Darlington", 162:"Derwentside",
                               163:"Durham", 164:"Easington", 165:"Sedgefield", 166:"Teesdale", 168:"Wear Valley", 169:"County Durham", 180:"Craven", 181:"Hambleton",
                               182:"Harrogate", 184:"Richmondshire", 185:"Ryedale", 186:"Scarborough", 187:"Selby", 189:"York", 200:"Bradford", 202:"Calderdale",
                               203:"Kirklees", 204:"Leeds", 206:"Wakefield", 210:"Barnsley", 211:"Doncaster", 213:"Rotherham", 215:"Sheffield", 228:"Kingston upon Hull, City of",
                               231:"East Riding of Yorkshire", 232:"North Lincolnshire", 233:"North East Lincolnshire", 240:"Hartlepool", 241:"Redcar and Cleveland", 243:"Middlesbrough", 245:"Stockton-on-Tees", 250:"Cannock Chase",
                               251:"East Staffordshire", 252:"Lichfield", 253:"Newcastle-under-Lyme", 254:"South Staffordshire", 255:"Stafford", 256:"Staffordshire Moorlands", 257:"Stoke-on-Trent", 258:"Tamworth",
                               270:"Bromsgrove", 273:"Malvern Hills", 274:"Redditch", 276:"Worcester", 277:"Wychavon", 278:"Wyre Forest", 279:"Bridgnorth", 280:"North Shropshire", 281:"Oswestry",
                               282:"Shrewsbury and Atcham", 283:"South Shropshire", 284:"Telford and Wrekin", 285:"Herefordshire, County of", 286:"Shropshire", 290:"North Warwickshire", 291:"Nuneaton and Bedworth", 292:"Rugby", 293:"Stratford-upon-Avon",
                               294:"Warwick", 300:"Birmingham", 302:"Coventry", 303:"Dudley", 305:"Sandwell", 306:"Solihull", 307:"Walsall", 309:"Wolverhampton",
                               320:"Amber Valley", 321:"Bolsover", 322:"Chesterfield", 323:"Derby", 324:"Erewash", 325:"High Peak", 327:"North East Derbyshire", 328:"South Derbyshire",
                               329:"Derbyshire Dales", 340:"Ashfield", 341:"Bassetlaw", 342:"Broxtowe", 343:"Gedling", 344:"Mansfield", 345:"Newark and Sherwood", 346:"Nottingham",
                               347:"Rushcliffe", 350:"Boston", 351:"East Lindsey", 352:"Lincoln", 353:"North Kesteven", 354:"South Holland", 355:"South Kesteven", 356:"West Lindsey", 360:"Blaby",
                               361:"Hinckley and Bosworth", 362:"Charnwood", 363:"Harborough", 364:"Leicester", 365:"Melton", 366:"North West Leicestershire", 367:"Oadby and Wigston", 368:"Rutland",
                               380:"Corby", 381:"Daventry", 382:"East Northamptonshire", 383:"Kettering", 384:"Northampton", 385:"South Northamptonshire", 386:"Wellingborough", 390:"Cambridge",
                               391:"East Cambridgeshire", 392:"Fenland", 393:"Huntingdonshire", 394:"Peterborough", 395:"South Cambridgeshire", 400:"Breckland", 401:"Broadland", 402:"Great Yarmouth",
                               404:"Norwich", 405:"North Norfolk", 406:"South Norfolk", 407:"King's Lynn and West Norfolk", 410:"Babergh", 411:"Forest Heath", 412:"Ipswich", 413:"Mid Suffolk",
                               414:"St. Edmundsbury", 415:"Suffolk Coastal", 416:"Waveney", 420:"Bedford", 421:"Luton", 422:"Mid Bedfordshire", 423:"South Bedfordshire", 424:"Central Bedfordshire",
                               430:"Broxbourne", 431:"Dacorum", 432:"East Hertfordshire", 433:"North Hertfordshire", 434:"St. Albans", 435:"Stevenage", 436:"Three Rivers", 437:"Watford",
                               438:"Welwyn Hatfield", 450:"Basildon", 451:"Braintree", 452:"Brentwood", 453:"Castle Point", 454:"Chelmsford", 455:"Colchester", 456:"Epping Forest", 457:"Harlow",
                               458:"Maldon", 459:"Rochford", 460:"Southend-on-Sea", 461:"Tendring", 462:"Thurrock", 463:"Uttlesford", 470:"Bracknell Forest", 471:"West Berkshire",
                               472:"Reading", 473:"Slough", 474:"Windsor and Maidenhead", 475:"Wokingham", 476:"Aylesbury Vale", 477:"South Bucks", 478:"Chiltern", 479:"Milton Keynes",
                               480:"Wycombe", 481:"Cherwell", 482:"Oxford", 483:"Vale of White Horse", 484:"South Oxfordshire", 485:"West Oxfordshire", 490:"Basingstoke and Deane", 491:"Eastleigh", 492:"Fareham",
                               493:"Gosport", 494:"Hart", 495:"Havant", 496:"New Forest", 497:"East Hampshire", 498:"Portsmouth", 499:"Rushmoor", 500:"Southampton",
                               501:"Test Valley", 502:"Winchester", 505:"Isle of Wight", 510:"Elmbridge", 511:"Guildford", 512:"Mole Valley", 513:"Reigate and Banstead", 514:"Runnymede",
                               515:"Surrey Heath", 516:"Tandridge", 517:"Waverley", 518:"Woking", 530:"Ashford", 531:"Canterbury", 532:"Dartford", 533:"Dover", 535:"Gravesham",
                               536:"Maidstone", 538:"Sevenoaks", 539:"Shepway", 540:"Swale", 541:"Thanet", 542:"Tonbridge and Malling", 543:"Tunbridge Wells", 544:"Medway",
                               551:"Eastbourne", 552:"Hastings", 554:"Lewes", 555:"Rother", 556:"Wealden", 557:"Adur", 558:"Arun", 559:"Chichester",
                               560:"Crawley", 562:"Horsham", 563:"Mid Sussex", 564:"Worthing", 565:"Brighton and Hove", 570:"City of London", 580:"East Devon", 581:"Exeter",
                               582:"North Devon", 583:"Plymouth", 584:"South Hams", 585:"Teignbridge", 586:"Mid Devon", 587:"Torbay", 588:"Torridge", 589:"West Devon",
                               590:"Caradon", 591:"Carrick", 592:"Kerrier", 593:"North Cornwall", 594:"Penwith", 595:"Restormel", 596:"Cornwall", 601:"Bristol, City of",
                               605:"North Somerset", 606:"Mendip", 607:"Sedgemoor", 608:"Taunton Deane", 609:"West Somerset", 610:"South Somerset", 611:"Bath and North East Somerset", 612:"South Gloucestershire",
                               620:"Cheltenham", 621:"Cotswold", 622:"Forest of Dean", 623:"Gloucester", 624:"Stroud", 625:"Tewkesbury", 630:"Kennet", 631:"North Wiltshire",
                               632:"Salisbury", 633:"Swindon", 634:"West Wiltshire", 635:"Wiltshire", 640:"Bournemouth", 641:"Christchurch", 642:"North Dorset", 643:"Poole",
                               644:"Purbeck", 645:"West Dorset", 646:"Weymouth and Portland", 647:"East Dorset", 720:"Isle of Anglesey", 721:"Conwy", 722:"Gwynedd", 723:"Denbighshire",
                               724:"Flintshire", 725:"Wrexham", 730:"Blaenau Gwent", 731:"Caerphilly", 732:"Monmouthshire", 733:"Newport", 734:"Torfaen", 740:"Bridgend",
                               741:"Cardiff", 742:"Merthyr Tydfil", 743:"Neath Port Talbot", 744:"Rhondda, Cynon, Taff", 745:"Swansea", 746:"The Vale of Glamorgan", 750:"Ceredigion", 751:"Carmarthenshire",
                               752:"Pembrokeshire", 753:"Powys", 910:"Aberdeen City", 911:"Aberdeenshire", 912:"Angus", 913:"Argyll and Bute", 914:"Scottish Borders", 915:"Clackmannanshire",
                               916:"West Dunbartonshire", 917:"Dumfries and Galloway", 918:"Dundee City", 919:"East Ayrshire", 920:"East Dunbartonshire", 921:"East Lothian", 922:"East Renfrewshire", 923:"Edinburgh, City of",
                               924:"Falkirk", 925:"Fife", 926:"Glasgow City", 927:"Highland", 928:"Inverclyde", 929:"Midlothian", 930:"Moray", 931:"North Ayrshire",
                               932:"North Lanarkshire", 933:"Orkney Islands", 934:"Perth and Kinross", 935:"Renfrewshire", 936:"Shetland Islands",
                               937:"South Ayrshire", 938:"South Lanarkshire", 939:"Stirling", 940:"West Lothian", 941:"Western Isles"}

LU_Local_Authority_Highway = {"S12000033":"Aberdeen City","S12000034":"Aberdeenshire","S12000041":"Angus","S12000035":"Argyll & Bute",
                              "E09000002":"Barking and Dagenham","E09000003":"Barnet","E08000016":"Barnsley","E06000022":"Bath and North East Somerset",
                              "E06000055":"Bedford","E09000004":"Bexley","E08000025":"Birmingham","E06000008":"Blackburn with Darwen",
                              "E06000009":"Blackpool","W06000019":"Blaenau Gwent","E08000001":"Bolton","E06000028":"Bournemouth",
                              "E06000036":"Bracknell Forest","E08000032":"Bradford","E09000005":"Brent","W06000013":"Bridgend",
                              "E06000043":"Brighton and Hove","E06000023":"Bristol, City of","E09000006":"Bromley","E10000002":"Buckinghamshire",
                              "E08000002":"Bury","W06000018":"Caerphilly","E08000033":"Calderdale","E10000003":"Cambridgeshire",
                              "E09000007":"Camden","W06000015":"Cardiff","W06000010":"Carmarthenshire","E06000056":"Central Bedfordshire",
                              "W06000008":"Ceredigion","E06000049":"Cheshire East","E06000050":"Cheshire West and Chester","E09000001":"City of London",
                              "S12000005":"Clackmannanshire","W06000003":"Conwy","E06000052":"Cornwall","E06000047":"County Durham",
                              "E08000026":"Coventry","E09000008":"Croydon","E10000006":"Cumbria","E06000005":"Darlington",
                              "W06000004":"Denbighshire","E06000015":"Derby","E10000007":"Derbyshire","E10000008":"Devon",
                              "E08000017":"Doncaster","E10000009":"Dorset","E08000027":"Dudley","S12000006":"Dumfries & Galloway",
                              "S12000042":"Dundee City","E09000009":"Ealing","S12000008":"East Ayrshire","S12000009":"East Dunbartonshire",
                              "S12000010":"East Lothian","S12000011":"East Renfrewshire","E06000011":"East Riding of Yorkshire","E10000011":"East Sussex",
                              "S12000036":"Edinburgh, City of","E09000010":"Enfield","E10000012":"Essex","S12000014":"Falkirk",
                              "S12000015":"Fife","W06000005":"Flintshire","E08000020":"Gateshead","S12000043":"Glasgow City",
                              "E10000013":"Gloucestershire","E09000011":"Greenwich","W06000002":"Gwynedd","E09000012":"Hackney",
                              "E06000006":"Halton","E09000013":"Hammersmith and Fulham","E10000014":"Hampshire","E09000014":"Haringey",
                              "E09000015":"Harrow","E06000001":"Hartlepool","E09000016":"Havering","E06000019":"Herefordshire, County of",
                              "E10000015":"Hertfordshire","S12000017":"Highland","E09000017":"Hillingdon","E09000018":"Hounslow",
                              "S12000018":"Inverclyde","W06000001":"Isle of Anglesey","E06000046":"Isle of Wight","E06000053":"Isles of Scilly",
                              "E09000019":"Islington","E09000020":"Kensington and Chelsea","E10000016":"Kent","E06000010":"Kingston upon Hull, City of",
                              "E09000021":"Kingston upon Thames","E08000034":"Kirklees","E08000011":"Knowsley","E09000022":"Lambeth",
                              "E10000017":"Lancashire","E08000035":"Leeds","E06000016":"Leicester","E10000018":"Leicestershire",
                              "E09000023":"Lewisham","E10000019":"Lincolnshire","E08000012":"Liverpool","EHEATHROW":"London Airport (Heathrow)",
                              "E06000032":"Luton","E08000003":"Manchester","E06000035":"Medway","W06000024":"Merthyr Tydfil",
                              "E09000024":"Merton","E06000002":"Middlesbrough","S12000019":"Midlothian","E06000042":"Milton Keynes",
                              "W06000021":"Monmouthshire","S12000020":"Moray","S12000013":"Na h-Eileanan an Iar (Western Isles)","W06000012":"Neath Port Talbot",
                              "E08000021":"Newcastle upon Tyne","E09000025":"Newham","W06000022":"Newport","E10000020":"Norfolk",
                              "S12000021":"North Ayrshire","E06000012":"North East Lincolnshire","S12000044":"North Lanarkshire","E06000013":"North Lincolnshire",
                              "E06000024":"North Somerset","E08000022":"North Tyneside","E10000023":"North Yorkshire","E10000021":"Northamptonshire",
                              "E06000048":"Northumberland","E06000018":"Nottingham","E10000024":"Nottinghamshire","E08000004":"Oldham",
                              "S12000023":"Orkney Islands","E10000025":"Oxfordshire","W06000009":"Pembrokeshire","S12000024":"Perth and Kinross",
                              "E06000031":"Peterborough","E06000026":"Plymouth","E06000029":"Poole","E06000044":"Portsmouth",
                              "W06000023":"Powys","E06000038":"Reading","E09000026":"Redbridge","E06000003":"Redcar and Cleveland",
                              "S12000038":"Renfrewshire","W06000016":"Rhondda, Cynon, Taff","E09000027":"Richmond upon Thames","E08000005":"Rochdale",
                              "E08000018":"Rotherham","E06000017":"Rutland","E08000006":"Salford","E08000028":"Sandwell",
                              "S12000026":"Scottish Borders","E08000014":"Sefton","E08000019":"Sheffield","S12000027":"Shetland Islands",
                              "E06000051":"Shropshire","E06000039":"Slough","E08000029":"Solihull","E10000027":"Somerset",
                              "S12000028":"South Ayrshire","E06000025":"South Gloucestershire","S12000029":"South Lanarkshire","E08000023":"South Tyneside",
                              "E06000045":"Southampton","E06000033":"Southend-on-Sea","E09000028":"Southwark","E08000013":"St. Helens",
                              "E10000028":"Staffordshire","S12000030":"Stirling","E08000007":"Stockport","E06000004":"Stockton-on-Tees",
                              "E06000021":"Stoke-on-Trent","E10000029":"Suffolk","E08000024":"Sunderland","E10000030":"Surrey",
                              "E09000029":"Sutton","W06000011":"Swansea","E06000030":"Swindon","E08000008":"Tameside",
                              "E06000020":"Telford and Wrekin","W06000014":"The Vale of Glamorgan","E06000034":"Thurrock","E06000027":"Torbay",
                              "W06000020":"Torfaen","E09000030":"Tower Hamlets","E08000009":"Trafford","E08000036":"Wakefield",
                              "E08000030":"Walsall","E09000031":"Waltham Forest","E09000032":"Wandsworth","E06000007":"Warrington",
                              "E10000031":"Warwickshire","E06000037":"West Berkshire","S12000039":"West Dunbartonshire","S12000040":"West Lothian",
                              "E10000032":"West Sussex","E09000033":"Westminster","E08000010":"Wigan","E06000054":"Wiltshire",
                              "E06000040":"Windsor and Maidenhead","E08000015":"Wirral","E06000041":"Wokingham","E08000031":"Wolverhampton",
                              "E10000034":"Worcestershire","W06000006":"Wrexham","E06000014":"York"}

LU_1st_Road_Class = {1:"Motorway", 2:"A(M)", 3:"A", 4:"B", 5:"C", 6:"Unclassified"}

LU_Road_Type = {1:"Roundabout", 2:"One way street", 3:"Dual carriageway", 6:"Single carriageway", 7:"Slip road",
                   9:"Unknown", 12:"One way street/Slip road", -1:"Data missing or out of range"}

LU_Junction_Detail = {0:"Not at junction or within 20 metres", 1:"Roundabout", 2:"Mini-roundabout", 3:"T or staggered junction",
                         5:"Slip road", 6:"Crossroads", 7:"More than 4 arms (not roundabout)", 8:"Private drive or entrance",
                         9:"Other junction", -1:"Data missing or out of range"}

LU_Junction_Control = {0:"Not at junction or within 20 metres", 1:"Authorised person", 2:"Auto traffic signal", 3:"Stop sign",
                       4:"Give way or uncontrolled", -1:"Data missing or out of range"}

LU_2nd_Road_Class = {0:"Not at junction or within 20 metres", 1:"Motorway", 2:"A(M)", 3:"A", 4:"B", 5:"C", 6:"Unclassified"}

LU_Pedestrian_Crossing_Human_Control = {0:"None within 50 metres", 1:"Control by school crossing patrol", 2:"Control by other authorised person",
                                        -1:"Data missing or out of range"}

LU_Pedestrian_Crossing_Physical_Facilities = {0:"No physical crossing facilities within 50 metres", 1:"Zebra", 4:"Pelican, puffin, toucan or similar non-junction pedestrian light crossing",
                                              5:"Pedestrian phase at traffic signal junction", 7:"Footbridge or subway", 8:"Central refuge", -1:"Data missing or out of range"}

LU_Light_Conditions = {1:"Daylight", 4:"Darkness - lights lit", 5:"Darkness - lights unlit", 6:"Darkness - no lighting",
                       7:"Darkness - lighting unknown", -1:"Data missing or out of range"}

LU_Weather_Conditions = {1:"Fine no high winds", 2:"Raining no high winds", 3:"Snowing no high winds", 4:"Fine + high winds",
                         5:"Raining + high winds", 6:"Snowing + high winds", 7:"Fog or mist", 8:"Other", 9:"Unknown", -1:"Data missing or out of range"}

LU_Road_Surface_Conditions = {1:"Dry", 2:"Wet or damp", 3:"Snow", 4:"Frost or ice", 5:"Flood over 3cm. deep", 6:"Oil or diesel",
                              7:"Mud", -1:"Data missing or out of range"}

LU_Special_Conditions_at_Site = {0:"None", 1:"Auto traffic signal - out", 2:"Auto signal part defective",
                                 3:"Road sign or marking defective or obscured", 4:"Roadworks", 5:"Road surface defective",
                                 6:"Oil or diesel", 7:"Mud", -1:"Data missing or out of range"}

LU_Carriageway_Hazards = {0:"None", 1:"Vehicle load on road", 2:"Other object on road", 3:"Previous accident",
                          4:"Dog on road", 5:"Other animal on road", 6:"Pedestrian in carriageway - not injured",
                          7:"Any animal in carriageway (except ridden horse)", -1:"Data missing or out of range"}

LU_Urban_or_Rural_Area = {1:"Urban", 2:"Rural", 3:"Unallocated"}

LU_Did_Police_Officer_Attend_Scene_of_Accident = {1:"Yes", 2:"No", 3:"No - accident was reported using a self completion  form (self rep only)"}

LU_Vehicle_Reference = {1:"Pedal cycle", 2:"Motorcycle 50cc and under", 3:"Motorcycle 125cc and under", 4:"Motorcycle over 125cc and up to 500cc",
                        5:"Motorcycle over 500cc", 8:"Taxi/Private hire car", 9:"Car", 10:"Minibus (8 - 16 passenger seats)",
                        11:"Bus or coach (17 or more pass seats)", 16:"Ridden horse", 17:"Agricultural vehicle",
                        18:"Tram", 19:"Van / Goods 3.5 tonnes mgw or under", 20:"Goods over 3.5t. and under 7.5t",
                        21:"Goods 7.5 tonnes mgw and over", 22:"Mobility scooter", 23:"Electric motorcycle",
                        90:"Other vehicle", 97:"Motorcycle - unknown cc", 98:"Goods vehicle - unknown weight",
                        -1:"Data missing or out of range"}

LU_Towing_and_Articulation = {0:"No tow/articulation", 1:"Articulated vehicle", 2:"Double or multiple trailer",
                              3:"Caravan", 4:"Single trailer", 5:"Other tow", -1:"Data missing or out of range"}

LU_Vehicle_Manoeuvre = {1:"Reversing", 2:"Parked", 3:"Waiting to go - held up", 4:"Slowing or stopping", 5:"Moving off",
                        6:"U-turn", 7:"Turning left", 8:"Waiting to turn left", 9:"Turning right", 10:"Waiting to turn right",
                        11:"Changing lane to left", 12:"Changing lane to right", 13:"Overtaking moving vehicle - offside",
                        14:"Overtaking static vehicle - offside", 15:"Overtaking - nearside", 16:"Going ahead left-hand bend",
                        17:"Going ahead right-hand bend", 18:"Going ahead other", -1:"Data missing or out of range"}

LU_Vehicle_Location_Restricted_Lane = {0:"On main c'way - not in restricted lane", 1:"Tram/Light rail track", 2:"Bus lane", 3:"Busway (including guided busway)",
                                       4:"Cycle lane (on main carriageway)", 5:"Cycleway or shared use footway (not part of  main carriageway)",
                                       6:"On lay-by or hard shoulder", 7:"Entering lay-by or hard shoulder", 8:"Leaving lay-by or hard shoulder",
                                       9:"Footway (pavement)", 10:"Not on carriageway", -1:"Data missing or out of range"}

LU_Junction_Location = {0:"Not at or within 20 metres of junction", 1:"Approaching junction or waiting/parked at junction approach",
                        2:"Cleared junction or waiting/parked at junction exit", 3:"Leaving roundabout", 4:"Entering roundabout",
                        5:"Leaving main road", 6:"Entering main road", 7:"Entering from slip road", 8:"Mid Junction - on roundabout or on main road",
                        -1:"Data missing or out of range"}

LU_Skidding_and_Overturning = {0:"None", 1:"Skidded", 2:"Skidded and overturned", 3:"Jackknifed",
                               4:"Jackknifed and overturned", 5:"Overturned", -1:"Data missing or out of range"}

LU_Hit_Object_in_Carriageway = {0:"None", 1:"Previous accident", 2:"Road works", 4:"Parked vehicle", 5:"Bridge (roof)",
                                6:"Bridge (side)", 7:"Bollard or refuge", 8:"Open door of vehicle", 9:"Central island of roundabout",
                                10:"Kerb", 11:"Other object", 12:"Any animal (except ridden horse)", -1:"Data missing or out of range"}

LU_Vehicle_Leaving_Carriageway = {0:"Did not leave carriageway", 1:"Nearside", 2:"Nearside and rebounded", 3:"Straight ahead at junction",
                                  4:"Offside on to central reservation", 5:"Offside on to centrl res + rebounded", 6:"Offside - crossed central reservation",
                                  7:"Offside", 8:"Offside and rebounded", -1:"Data missing or out of range"}

LU_Hit_Object_off_Carriageway = {0:"None", 1:"Road sign or traffic signal", 2:"Lamp post", 3:"Telegraph or electricity pole",
                                 4:"Tree", 5:"Bus stop or bus shelter", 6:"Central crash barrier", 7:"Near/Offside crash barrier",
                                 8:"Submerged in water", 9:"Entered ditch", 10:"Other permanent object", 11:"Wall or fence",
                                 -1:"Data missing or out of range"}

LU_1st_Point_of_Impact = {0:"Did not impact", 1:"Front", 2:"Back", 3:"Offside", 4:"Nearside", -1:"Data missing or out of range"}

LU_Was_Vehicle_Left_Hand_Drive = {1:"No", 2:"Yes", -1:"Data missing or out of range"}

LU_Journey_Purpose_of_Driver = {1:"Journey as part of work", 2:"Commuting to/from work", 3:"Taking pupil to/from school",
                                4:"Pupil riding to/from school", 5:"Other", 6:"Not known", 15:"Other/Not known (2005-10)",
                                -1:"Data missing or out of range"}

LU_Sex_of_Driver = {1:"Male", 2:"Female", 3:"Not known", -1:"Data missing or out of range"}

# I'm assuming that this is the same for casualty and driver
LU_Age_Band = {1:"0 - 5", 2:"6 - 10", 3:"11 - 15", 4:"16 - 20", 5:"21 - 25", 6:"26 - 35",
               7:"36 - 45", 8:"46 - 55", 9:"56 - 65", 10:"66 - 75", 11:"Over 75", -1:"Data missing or out of range"}

LU_Vehicle_Type= {1:"Petrol", 2:"Heavy oil", 3:"Electric", 4:"Steam", 5:"Gas", 6:"Petrol/Gas (LPG)",
                        7:"Gas/Bi-fuel", 8:"Hybrid electric", 9:"Gas Diesel", 10:"New fuel technology",
                        11:"Fuel cells", 12:"Electric diesel",  -1:"Undefined"}

# Not sure about this one
LU_Casualty_Reference = {1:"Driver or rider", 2:"Passenger", 3:"Pedestrian"}

LU_Sex_of_Casualty = {1:"Male", 2:"Female", -1:"Data missing or out of range"}

# Assuming this is the same for driver and casualty
LU_Age = {-1:np.nan} # The label is 0-120 --> 0-120, therefore re-classifying the missing data as NaN

LU_Casualty_Severity = {1:"Fatal", 2:"Serious", 3:"Slight"}

LU_Pedestrian_Location = {0:"Not a Pedestrian", 1:"Crossing on pedestrian crossing facility", 2:"Crossing in zig-zag approach lines",
                      3:"Crossing in zig-zag exit lines", 4:"Crossing elsewhere within 50m. of pedestrian crossing",
                      5:"In carriageway, crossing elsewhere", 6:"On footway or verge", 7:"On refuge, central island or central reservation",
                      8:"In centre of carriageway - not on refuge, island or central reservation", 9:"In carriageway, not crossing",
                      10:"Unknown or other", -1:"Data missing or out of range"}

LU_Pedestrian_Movement = {0:"Not a Pedestrian", 1:"Crossing from driver's nearside", 2:"Crossing from nearside - masked by parked or stationary vehicle",
                          3:"Crossing from driver's offside", 4:"Crossing from offside - masked by  parked or stationary vehicle",
                          5:"In carriageway, stationary - not crossing  (standing or playing)", 6:"In carriageway, stationary - not crossing  (standing or playing) - masked by parked or stationary vehicle",
                          7:"Walking along in carriageway, facing traffic", 8:"Walking along in carriageway, back to traffic",
                          9:"Unknown or other", -1:"Data missing or out of range"}

LU_Car_Passenger = {0:"Not car passenger", 1:"Front seat passenger", 2:"Rear seat passenger", -1:"Data missing or out of range"}

LU_Bus_or_Coach_Passenger = {0:"Not a bus or coach passenger", 1:"Boarding", 2:"Alighting", 3:"Standing passenger",
                             4:"Seated passenger", -1:"Data missing or out of range"}

LU_Pedestrian_Road_Maintenance_Worker = {0:"No / Not applicable", 1:"Yes", 2:"Not Known", -1:"Data missing or out of range"}

LU_Casualty_Type = {0:"Pedestrian", 1:"Cyclist", 2:"Motorcycle 50cc and under rider or passenger", 3:"Motorcycle 125cc and under rider or passenger",
                    4:"Motorcycle over 125cc and up to 500cc rider or  passenger", 5:"Motorcycle over 500cc rider or passenger",
                    8:"Taxi/Private hire car occupant", 9:"Car occupant", 10:"Minibus (8 - 16 passenger seats) occupant",
                    11:"Bus or coach occupant (17 or more pass seats)", 16:"Horse rider", 17:"Agricultural vehicle occupant",
                    18:"Tram occupant", 19:"Van / Goods vehicle (3.5 tonnes mgw or under) occupant", 20:"Goods vehicle (over 3.5t. and under 7.5t.) occupant",
                    21:"Goods vehicle (7.5 tonnes mgw and over) occupant", 22:"Mobility scooter rider", 23:"Electric motorcycle rider or passenger",
                    90:"Other vehicle occupant", 97:"Motorcycle - unknown cc rider or passenger", 98:"Goods vehicle (unknown weight) occupant"}

LU_Casualty_IMD_Decile = {1:"Most deprived 10%", 2:"More deprived 10-20%", 3:"More deprived 20-30%", 4:"More deprived 30-40%",
                          5:"More deprived 40-50%", 6:"Less deprived 40-50%", 7:"Less deprived 30-40%", 8:"Less deprived 20-30%",
                          9:"Less deprived 10-20%", 10:"Least deprived 10%", -1:"Data missing or out of range"}

LU_Casualty_Home_Area_Type = {1:"Urban area", 2:"Small town", 3:"Rural", -1:"Data missing or out of range"}

LU_Casualty_Class = {1:"Driver or rider", 2:"Passenger", 3:"Pedestrian"}

LU_CleanUp = {-1:np.nan}

"""
# Changing the DataFrame data to be useful human-readable information
"""

# Creating lists of the DataFrames
list_Acc = [df_Acc_2016, df_Acc_2015, df_Acc_2014, df_Acc_2013, df_Acc_2012, df_Acc_2011, df_Acc_2010, df_Acc_2009]
list_Cas = [df_Cas_2016, df_Cas_2015, df_Cas_2014, df_Cas_2013, df_Cas_2012, df_Cas_2011,df_Cas_2010,df_Cas_2009]
list_Veh = [df_Veh_2016, df_Veh_2015, df_Veh_2014, df_Veh_2013, df_Veh_2012, df_Veh_2011, df_Veh_2010, df_Veh_2009]

# Looping through the DataFrames to amend the data

# Accidents

for item in list_Acc:

    """ For loop to replace the numbers with information in accidents"""

    item["Police_Force"].replace(LU_Police_Force, inplace=True)
    item["Accident_Severity"].replace(LU_Accident_Severity, inplace=True)
    item["Local_Authority_(District)"].replace(LU_Local_Authority_District, inplace=True)
    item["Local_Authority_(Highway)"].replace(LU_Local_Authority_Highway, inplace=True)
    item["1st_Road_Class"].replace(LU_1st_Road_Class, inplace=True)
    item["Road_Type"].replace(LU_Road_Type, inplace=True)
    item["Junction_Detail"].replace(LU_Junction_Detail, inplace=True)
    item["Junction_Control"].replace(LU_Junction_Control, inplace=True)
    item["2nd_Road_Class"].replace(LU_2nd_Road_Class, inplace=True)
    item["Pedestrian_Crossing-Human_Control"].replace(LU_Pedestrian_Crossing_Human_Control, inplace=True)
    item["Pedestrian_Crossing-Physical_Facilities"].replace(LU_Pedestrian_Crossing_Physical_Facilities, inplace=True)
    item["Light_Conditions"].replace(LU_Light_Conditions, inplace=True)
    item["Weather_Conditions"].replace(LU_Weather_Conditions, inplace=True)
    item["Road_Surface_Conditions"].replace(LU_Road_Surface_Conditions, inplace=True)
    item["Special_Conditions_at_Site"].replace(LU_Special_Conditions_at_Site, inplace=True)
    item["Carriageway_Hazards"].replace(LU_Carriageway_Hazards, inplace=True)
    item["Urban_or_Rural_Area"].replace(LU_Urban_or_Rural_Area, inplace=True)
    item["Did_Police_Officer_Attend_Scene_of_Accident"].replace(LU_Did_Police_Officer_Attend_Scene_of_Accident, inplace=True)
    item["Day_of_Week"].replace(LU_Day_of_Week, inplace=True)

    # -1 appears in the numerical columns. Clear intention as missing or unknown. To remove as effecting the statistics.
    item["2nd_Road_Number"].replace(LU_CleanUp, inplace=True)

# Casualties

for item in list_Cas:

    """ For loop to replace the numbers with information in Casualties"""

    #item["Vehicle_Reference"].replace(LU_Vehicle_Reference, inplace=True) # No relevant look-up table
    item["Casualty_Reference"].replace(LU_Casualty_Reference, inplace=True)
    item["Sex_of_Casualty"].replace(LU_Sex_of_Casualty, inplace=True)
    item["Age_Band_of_Casualty"].replace(LU_Age_Band, inplace=True)
    item["Casualty_Severity"].replace(LU_Casualty_Severity, inplace=True)
    item["Pedestrian_Location"].replace(LU_Pedestrian_Location, inplace=True)
    item["Pedestrian_Movement"].replace(LU_Pedestrian_Movement, inplace=True)
    item["Car_Passenger"].replace(LU_Car_Passenger, inplace=True)
    item["Bus_or_Coach_Passenger"].replace(LU_Bus_or_Coach_Passenger, inplace=True)
    item["Pedestrian_Road_Maintenance_Worker"].replace(LU_Pedestrian_Road_Maintenance_Worker, inplace=True)
    item["Casualty_Type"].replace(LU_Casualty_Type, inplace=True)
    item["Casualty_Home_Area_Type"].replace(LU_Casualty_Home_Area_Type, inplace=True)
    item["Casualty_Class"].replace(LU_Casualty_Class, inplace=True)

# Cleaning up exceptions

for item in [df_Cas_2016, df_Cas_2015]:
    item["Casualty_IMD_Decile"].replace(LU_Casualty_IMD_Decile, inplace=True) # Only exists in 2016 & 2015

for item in [df_Cas_2016, df_Cas_2015, df_Cas_2014]:
    # -1 appears in the numerical columns. Clear intention as missing or unknown. To remove as effecting the statistics.
    item["Age_of_Casualty"].replace(LU_CleanUp, inplace=True) # Only exists in 2016, 2015, & 2014

# Vehicles

for item in list_Veh:

    """ For loop to replace the numbers with information in Casualties"""

    # item["Vehicle_Reference"].replace(LU_Vehicle_Reference, inplace=True) # No relevant look-up table
    item["Vehicle_Type"].replace(LU_Vehicle_Reference, inplace=True) # Mismatched information!
    item["Towing_and_Articulation"].replace(LU_Towing_and_Articulation, inplace=True)
    item["Vehicle_Manoeuvre"].replace(LU_Vehicle_Manoeuvre, inplace=True)
    item["Vehicle_Location-Restricted_Lane"].replace(LU_Vehicle_Location_Restricted_Lane, inplace=True)
    item["Junction_Location"].replace(LU_Junction_Location, inplace=True)
    item["Skidding_and_Overturning"].replace(LU_Skidding_and_Overturning, inplace=True)
    item["Hit_Object_in_Carriageway"].replace(LU_Hit_Object_in_Carriageway, inplace=True)
    item["Vehicle_Leaving_Carriageway"].replace(LU_Vehicle_Leaving_Carriageway, inplace=True)
    item["Hit_Object_off_Carriageway"].replace(LU_Hit_Object_off_Carriageway, inplace=True)
    item["1st_Point_of_Impact"].replace(LU_1st_Point_of_Impact, inplace=True)
    item["Was_Vehicle_Left_Hand_Drive?"].replace(LU_Was_Vehicle_Left_Hand_Drive, inplace=True)
    item["Journey_Purpose_of_Driver"].replace(LU_Journey_Purpose_of_Driver, inplace=True)
    item["Sex_of_Driver"].replace(LU_Sex_of_Driver, inplace=True)
    item["Age_Band_of_Driver"].replace(LU_Age_Band, inplace=True)
    item["Driver_IMD_Decile"].replace(LU_Casualty_IMD_Decile, inplace=True)
    item["Driver_Home_Area_Type"].replace(LU_Casualty_Home_Area_Type, inplace=True)
    item["Propulsion_Code"].replace(LU_Vehicle_Type, inplace=True)

    # -1 appears in the numerical columns. Clear intention as missing or unknown. To remove as effecting the statistics.
    item["Engine_Capacity_(CC)"].replace(LU_CleanUp, inplace=True)
    item["Age_of_Vehicle"].replace(LU_CleanUp, inplace=True)

# Cleaning up exceptions

for item in [df_Veh_2016, df_Veh_2015]:
    item["Vehicle_IMD_Decile"].replace(LU_Casualty_IMD_Decile, inplace=True) # Only exists in 2016 & 2015

for item in [df_Veh_2016, df_Veh_2015, df_Veh_2014]:
    # -1 appears in the numerical columns. Clear intention as missing or unknown. To remove as effecting the statistics.
    item["Age_of_Driver"].replace(LU_CleanUp, inplace=True) # Only exists in 2016, 2015, & 2014

"""
# Saving the newly edited DataFrames as .csv files for faster access and processing
"""

df_Acc_2016.to_csv("Accidents_2016", sep=",", index=True)
df_Acc_2015.to_csv("Accidents_2015", sep=",", index=True)
df_Acc_2014.to_csv("Accidents_2014", sep=",", index=True)
df_Acc_2013.to_csv("Accidents_2013", sep=",", index=True)
df_Acc_2012.to_csv("Accidents_2012", sep=",", index=True)
df_Acc_2011.to_csv("Accidents_2011", sep=",", index=True)
df_Acc_2010.to_csv("Accidents_2010", sep=",", index=True)
df_Acc_2009.to_csv("Accidents_2009", sep=",", index=True)

df_Cas_2016.to_csv("Casualties_2016", sep=",", index=True)
df_Cas_2015.to_csv("Casualties_2015", sep=",", index=True)
df_Cas_2014.to_csv("Casualties_2014", sep=",", index=True)
df_Cas_2013.to_csv("Casualties_2013", sep=",", index=True)
df_Cas_2012.to_csv("Casualties_2012", sep=",", index=True)
df_Cas_2011.to_csv("Casualties_2011", sep=",", index=True)
df_Cas_2010.to_csv("Casualties_2010", sep=",", index=True)
df_Cas_2009.to_csv("Casualties_2009", sep=",", index=True)

df_Veh_2016.to_csv("Vehicle_2016", sep=",", index=True)
df_Veh_2015.to_csv("Vehicle_2015", sep=",", index=True)
df_Veh_2014.to_csv("Vehicle_2014", sep=",", index=True)
df_Veh_2013.to_csv("Vehicle_2013", sep=",", index=True)
df_Veh_2012.to_csv("Vehicle_2012", sep=",", index=True)
df_Veh_2011.to_csv("Vehicle_2011", sep=",", index=True)
df_Veh_2010.to_csv("Vehicle_2010", sep=",", index=True)
df_Veh_2009.to_csv("Vehicle_2009", sep=",", index=True)

"""
# Merging the tables into an All table for 5 years
"""

# All 2016

Temp = pd.merge(df_Acc_2016, df_Veh_2016, left_index=True, right_index=True, how="outer")
All_Of_2016 = pd.merge(Temp, df_Cas_2016, left_index=True, right_index=True, how="outer")
All_Of_2016["Collection_Year"] = 2016
All_Of_2016.to_csv("All_Of_2016", sep=",", index=True)

# All 2015

Temp = pd.merge(df_Acc_2015, df_Veh_2015, left_index=True, right_index=True, how="outer")
All_Of_2015 = pd.merge(Temp, df_Cas_2015, left_index=True, right_index=True, how="outer")
All_Of_2015["Collection_Year"] = 2015
All_Of_2015.to_csv("All_Of_2015", sep=",", index=True)

# All 2014

Temp = pd.merge(df_Acc_2014, df_Veh_2014, left_index=True, right_index=True, how="outer")
All_Of_2014 = pd.merge(Temp, df_Cas_2014, left_index=True, right_index=True, how="outer")
All_Of_2014["Collection_Year"] = 2014
All_Of_2014.to_csv("All_Of_2014", sep=",", index=True)

# All 2013

Temp = pd.merge(df_Acc_2013, df_Veh_2013, left_index=True, right_index=True, how="outer")
All_Of_2013 = pd.merge(Temp, df_Cas_2013, left_index=True, right_index=True, how="outer")
All_Of_2013["Collection_Year"] = 2013
All_Of_2013.to_csv("All_Of_2013", sep=",", index=True)

# All 2012

Temp = pd.merge(df_Acc_2012, df_Veh_2012, left_index=True, right_index=True, how="outer")
All_Of_2012 = pd.merge(Temp, df_Cas_2012, left_index=True, right_index=True, how="outer")
All_Of_2012["Collection_Year"] = 2012
All_Of_2012.to_csv("All_Of_2012", sep=",", index=True)
