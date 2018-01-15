
"""
# Import libraries as their usual aliases
"""

import pandas as pd
import numpy as np

"""
# Define lists and functions
"""

DistrictList = ["Westminster", "Camden", "Islington", "Hackney", "Tower Hamlets", "Greenwich", "Lewisham", "Southwark",
                "Lambeth", "Wandsworth", "Hammersmith and Fulham", "Kensington and Chelsea", "Waltham Forest", "Redbridge", "Havering", "Barking and Dagenham",
                "Newham", "Bexley", "Bromley", "Croydon", "Sutton", "Merton", "Kingston upon Thames", "Richmond upon Thames",
                "Hounslow", "Hillingdon", "Ealing", "Brent", "Harrow", "Barnet", "Haringey", "Enfield",
                "Hertsmere", "Epsom and Ewell", "Spelthorne", "London Airport (Heathrow)", "Allerdale", "Barrow-in-Furness", "Carlisle", "Copeland",
                "Eden", "South Lakeland", "Blackburn with Darwen", "Blackpool", "Burnley", "Chorley", "Fylde", "Hyndburn",
                "Lancaster", "Pendle", "Preston", "Ribble Valley", "Rossendale", "South Ribble", "West Lancashire", "Wyre",
                "Knowsley", "Liverpool", "St. Helens", "Sefton", "Wirral", "Bolton", "Bury", "Manchester",
                "Oldham", "Rochdale", "Salford", "Stockport", "Tameside", "Trafford", "Wigan", "Chester",
                "Congleton", "Crewe and Nantwich", "Ellesmere Port and Neston", "Halton", "Macclesfield", "Vale Royal", "Warrington", "Cheshire East",
                "Cheshire West and Chester", "Northumberland", "Alnwick", "Berwick-upon-Tweed", "Blyth Valley", "Castle Morpeth", "Tynedale", "Wansbeck",
                "Gateshead", "Newcastle upon Tyne", "North Tyneside", "South Tyneside", "Sunderland", "Chester-le-Street", "Darlington", "Derwentside",
                "Durham", "Easington", "Sedgefield", "Teesdale", "Wear Valley", "County Durham", "Craven", "Hambleton",
                "Harrogate", "Richmondshire", "Ryedale", "Scarborough", "Selby", "York", "Bradford", "Calderdale",
                "Kirklees", "Leeds", "Wakefield", "Barnsley", "Doncaster", "Rotherham", "Sheffield", "Kingston upon Hull, City of",
                "East Riding of Yorkshire", "North Lincolnshire", "North East Lincolnshire", "Hartlepool", "Redcar and Cleveland", "Middlesbrough", "Stockton-on-Tees", "Cannock Chase",
                "East Staffordshire", "Lichfield", "Newcastle-under-Lyme", "South Staffordshire", "Stafford", "Staffordshire Moorlands", "Stoke-on-Trent", "Tamworth",
                "Bromsgrove", "Malvern Hills", "Redditch", "Worcester", "Wychavon", "Wyre Forest", "Bridgnorth", "North Shropshire", "Oswestry",
                "Shrewsbury and Atcham", "South Shropshire", "Telford and Wrekin", "Herefordshire, County of", "Shropshire", "North Warwickshire", "Nuneaton and Bedworth", "Rugby", "Stratford-upon-Avon",
                "Warwick", "Birmingham", "Coventry", "Dudley", "Sandwell", "Solihull", "Walsall", "Wolverhampton",
                "Amber Valley", "Bolsover", "Chesterfield", "Derby", "Erewash", "High Peak", "North East Derbyshire", "South Derbyshire",
                "Derbyshire Dales", "Ashfield", "Bassetlaw", "Broxtowe", "Gedling", "Mansfield", "Newark and Sherwood", "Nottingham",
                "Rushcliffe", "Boston", "East Lindsey", "Lincoln", "North Kesteven", "South Holland", "South Kesteven", "West Lindsey", "Blaby",
                "Hinckley and Bosworth", "Charnwood", "Harborough", "Leicester", "Melton", "North West Leicestershire", "Oadby and Wigston", "Rutland",
                "Corby", "Daventry", "East Northamptonshire", "Kettering", "Northampton", "South Northamptonshire", "Wellingborough", "Cambridge",
                "East Cambridgeshire", "Fenland", "Huntingdonshire", "Peterborough", "South Cambridgeshire", "Breckland", "Broadland", "Great Yarmouth",
                "Norwich", "North Norfolk", "South Norfolk", "King's Lynn and West Norfolk", "Babergh", "Forest Heath", "Ipswich", "Mid Suffolk",
                "St. Edmundsbury", "Suffolk Coastal", "Waveney", "Bedford", "Luton", "Mid Bedfordshire", "South Bedfordshire", "Central Bedfordshire",
                "Broxbourne", "Dacorum", "East Hertfordshire", "North Hertfordshire", "St. Albans", "Stevenage", "Three Rivers", "Watford",
                "Welwyn Hatfield", "Basildon", "Braintree", "Brentwood", "Castle Point", "Chelmsford", "Colchester", "Epping Forest", "Harlow",
                "Maldon", "Rochford", "Southend-on-Sea", "Tendring", "Thurrock", "Uttlesford", "Bracknell Forest", "West Berkshire",
                "Reading", "Slough", "Windsor and Maidenhead", "Wokingham", "Aylesbury Vale", "South Bucks", "Chiltern", "Milton Keynes",
                "Wycombe", "Cherwell", "Oxford", "Vale of White Horse", "South Oxfordshire", "West Oxfordshire", "Basingstoke and Deane", "Eastleigh", "Fareham",
                "Gosport", "Hart", "Havant", "New Forest", "East Hampshire", "Portsmouth", "Rushmoor", "Southampton",
                "Test Valley", "Winchester", "Isle of Wight", "Elmbridge", "Guildford", "Mole Valley", "Reigate and Banstead", "Runnymede",
                "Surrey Heath", "Tandridge", "Waverley", "Woking", "Ashford", "Canterbury", "Dartford", "Dover", "Gravesham",
                "Maidstone", "Sevenoaks", "Shepway", "Swale", "Thanet", "Tonbridge and Malling", "Tunbridge Wells", "Medway",
                "Eastbourne", "Hastings", "Lewes", "Rother", "Wealden", "Adur", "Arun", "Chichester",
                "Crawley", "Horsham", "Mid Sussex", "Worthing", "Brighton and Hove", "City of London", "East Devon", "Exeter",
                "North Devon", "Plymouth", "South Hams", "Teignbridge", "Mid Devon", "Torbay", "Torridge", "West Devon",
                "Caradon", "Carrick", "Kerrier", "North Cornwall", "Penwith", "Restormel", "Cornwall", "Bristol, City of",
                "North Somerset", "Mendip", "Sedgemoor", "Taunton Deane", "West Somerset", "South Somerset", "Bath and North East Somerset", "South Gloucestershire",
                "Cheltenham", "Cotswold", "Forest of Dean", "Gloucester", "Stroud", "Tewkesbury", "Kennet", "North Wiltshire",
                "Salisbury", "Swindon", "West Wiltshire", "Wiltshire", "Bournemouth", "Christchurch", "North Dorset", "Poole",
                "Purbeck", "West Dorset", "Weymouth and Portland", "East Dorset", "Isle of Anglesey", "Conwy", "Gwynedd", "Denbighshire",
                "Flintshire", "Wrexham", "Blaenau Gwent", "Caerphilly", "Monmouthshire", "Newport", "Torfaen", "Bridgend",
                "Cardiff", "Merthyr Tydfil", "Neath Port Talbot", "Rhondda, Cynon, Taff", "Swansea", "The Vale of Glamorgan", "Ceredigion", "Carmarthenshire",
                "Pembrokeshire", "Powys", "Aberdeen City", "Aberdeenshire", "Angus", "Argyll and Bute", "Scottish Borders", "Clackmannanshire",
                "West Dunbartonshire", "Dumfries and Galloway", "Dundee City", "East Ayrshire", "East Dunbartonshire", "East Lothian", "East Renfrewshire", "Edinburgh, City of",
                "Falkirk", "Fife", "Glasgow City", "Highland", "Inverclyde", "Midlothian", "Moray", "North Ayrshire",
                "North Lanarkshire", "Orkney Islands", "Perth and Kinross", "Renfrewshire", "Shetland Islands",
                "South Ayrshire", "South Lanarkshire", "Stirling", "West Lothian", "Western Isles"]

"""
# Test Bench
"""
DATA = {"Col1":[1, 2, 3, 4, 5],
        "Col2":["Male", "Female", "Female", "Male", "Male"],
        "Col3":["01/11/2016", '01/11/2016', '02/11/2016', '02/11/2016', '03/11/2016'],
        "Col4": ["Durham", "Durham", "New", "Ips", "Durham"]
        }

df = pd.DataFrame(DATA)

# Convert column from string into DateTime
df['Datetime'] = pd.to_datetime(df['Col3'], format="%d/%m/%Y")

# Set the index
df = df.set_index('Datetime')

# Create new DataFrame with districts counted per day
dfNew = df.groupby([df.index, df.Col4]).Col4.count().reset_index(level=1, name='Counts')

# Reduce DataFrame to certain amount of counts per day for a given district
dfReduced = dfNew.loc[np.logical_and(dfNew.Col4=="Durham", dfNew.Counts >= 1)]

# Check if that district for that count occurs every day in a calendar year
# (!) Simply check the length of the DataFrame. If it is 365 then it occured every day for a year
#print(len(dfReduced))

"""
# Let's try it with the actual DataFrame ...
"""

df = pd.read_csv(r"C:\Users\Matthew\Documents\PyCharm\CodingChallenges\SKY\EditedDataFiles\2016Reduced")

# Convert column from string into DateTime
df['Datetime'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")

# Set the index
df = df.set_index('Datetime')

print(df.head())

# Create new DataFrame with districts counted per day
dfNew = df.groupby([df.index, df["Local_Authority_(District)"]])["Local_Authority_(District)"].count().reset_index(level=1, name='Counts')

# Reduce DataFrame to certain amount of counts per day for a given district
#dfRed = dfNew.loc[np.logical_and(dfNew["Local_Authority_(District)"]=="Westminster", dfNew.Counts >= 1)]
dfRed = dfNew.loc[dfNew["Local_Authority_(District)"]=="Westminster"]

print(len(dfRed))

print(dfRed.head())
print(dfRed.tail())

# Defining the list of Districts

CountList = []
for item in DistrictList:
        dfRed = dfNew.loc[np.logical_and(dfNew["Local_Authority_(District)"] == str(item), dfNew.Counts >= 1)]
        Count = len(dfRed)
        CountList.append(len(dfRed))
        if Count >= 312:
                print(item, len(dfRed))