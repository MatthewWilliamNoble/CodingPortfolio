# Important: To correct the cut-off, adjust the bottom off-set to 0.21

########## Importing the relevant libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

########## Creating the pandas data frame

Path = r"C:\Users\Matthew\Documents\Pycharm\DataScienceProjects\Pokemon\PokemonData.csv"
df = pd.read_csv(Path, index_col=0)

########## Sub-dividing into the relevant categories

Gen1 = df["Generation"] == 1
Gen2 = df["Generation"] == 2
Gen3 = df["Generation"] == 3
Gen4 = df["Generation"] == 4
Gen5 = df["Generation"] == 5
Gen6 = df["Generation"] == 6

T1Nor = df["Type_1"] == "Normal"
T1Fig = df["Type_1"] == "Fighting"
T1Fly = df["Type_1"] == "Flying"
T1Poi = df["Type_1"] == "Poison"
T1Gro = df["Type_1"] == "Ground"
T1Roc = df["Type_1"] == "Rock"
T1Bug = df["Type_1"] == "Bug"
T1Gho = df["Type_1"] == "Ghost"
T1Ste = df["Type_1"] == "Steel"
T1Fir = df["Type_1"] == "Fire"
T1Wat = df["Type_1"] == "Water"
T1Gra = df["Type_1"] == "Grass"
T1Ele = df["Type_1"] == "Electric"
T1Psy = df["Type_1"] == "Psychic"
T1Ice = df["Type_1"] == "Ice"
T1Dra = df["Type_1"] == "Dragon"
T1Dar = df["Type_1"] == "Dark"
T1Fai = df["Type_1"] == "Fairy"

T2Nor = df["Type_2"] == "Normal"
T2Fig = df["Type_2"] == "Fighting"
T2Fly = df["Type_2"] == "Flying"
T2Poi = df["Type_2"] == "Poison"
T2Gro = df["Type_2"] == "Ground"
T2Roc = df["Type_2"] == "Rock"
T2Bug = df["Type_2"] == "Bug"
T2Gho = df["Type_2"] == "Ghost"
T2Ste = df["Type_2"] == "Steel"
T2Fir = df["Type_2"] == "Fire"
T2Wat = df["Type_2"] == "Water"
T2Gra = df["Type_2"] == "Grass"
T2Ele = df["Type_2"] == "Electric"
T2Psy = df["Type_2"] == "Psychic"
T2Ice = df["Type_2"] == "Ice"
T2Dra = df["Type_2"] == "Dragon"
T2Dar = df["Type_2"] == "Dark"
T2Fai = df["Type_2"] == "Fairy"

AllNor = np.logical_or(T1Nor, T2Nor)
AllFig = np.logical_or(T1Fig, T2Fig)
AllFly = np.logical_or(T1Fly, T2Fly)
AllPoi = np.logical_or(T1Poi, T2Poi)
AllGro = np.logical_or(T1Gro, T2Gro)
AllRoc = np.logical_or(T1Roc, T2Roc)
AllBug = np.logical_or(T1Bug, T2Bug)
AllGho = np.logical_or(T1Gho, T2Gho)
AllSte = np.logical_or(T1Ste, T2Ste)
AllFir = np.logical_or(T1Fir, T2Fir)
AllWat = np.logical_or(T1Wat, T2Wat)
AllGra = np.logical_or(T1Gra, T2Gra)
AllEle = np.logical_or(T1Ele, T2Ele)
AllPsy = np.logical_or(T1Psy, T2Psy)
AllIce = np.logical_or(T1Ice, T2Ice)
AllDra = np.logical_or(T1Dra, T2Dra)
AllDar = np.logical_or(T1Dar, T2Dar)
AllFai = np.logical_or(T1Fai, T2Fai)

########## Plotting information

# All Generations
T1NorAllGen = df.loc[T1Nor]
T1FigAllGen = df.loc[T1Fig]
T1FlyAllGen = df.loc[T1Fly]
T1PoiAllGen = df.loc[T1Poi]
T1GroAllGen = df.loc[T1Gro]
T1RocAllGen = df.loc[T1Roc]
T1BugAllGen = df.loc[T1Bug]
T1GhoAllGen = df.loc[T1Gho]
T1SteAllGen = df.loc[T1Ste]
T1FirAllGen = df.loc[T1Fir]
T1WatAllGen = df.loc[T1Wat]
T1GraAllGen = df.loc[T1Gra]
T1EleAllGen = df.loc[T1Ele]
T1PsyAllGen = df.loc[T1Psy]
T1IceAllGen = df.loc[T1Ice]
T1DraAllGen = df.loc[T1Dra]
T1DarAllGen = df.loc[T1Dar]
T1FaiAllGen = df.loc[T1Fai]

T2NorAllGen = df.loc[T2Nor]
T2FigAllGen = df.loc[T2Fig]
T2FlyAllGen = df.loc[T2Fly]
T2PoiAllGen = df.loc[T2Poi]
T2GroAllGen = df.loc[T2Gro]
T2RocAllGen = df.loc[T2Roc]
T2BugAllGen = df.loc[T2Bug]
T2GhoAllGen = df.loc[T2Gho]
T2SteAllGen = df.loc[T2Ste]
T2FirAllGen = df.loc[T2Fir]
T2WatAllGen = df.loc[T2Wat]
T2GraAllGen = df.loc[T2Gra]
T2EleAllGen = df.loc[T2Ele]
T2PsyAllGen = df.loc[T2Psy]
T2IceAllGen = df.loc[T2Ice]
T2DraAllGen = df.loc[T2Dra]
T2DarAllGen = df.loc[T2Dar]
T2FaiAllGen = df.loc[T2Fai]

AllNorAllGen = df.loc[AllNor]
AllFigAllGen = df.loc[AllFig]
AllFlyAllGen = df.loc[AllFly]
AllPoiAllGen = df.loc[AllPoi]
AllGroAllGen = df.loc[AllGro]
AllRocAllGen = df.loc[AllRoc]
AllBugAllGen = df.loc[AllBug]
AllGhoAllGen = df.loc[AllGho]
AllSteAllGen = df.loc[AllSte]
AllFirAllGen = df.loc[AllFir]
AllWatAllGen = df.loc[AllWat]
AllGraAllGen = df.loc[AllGra]
AllEleAllGen = df.loc[AllEle]
AllPsyAllGen = df.loc[AllPsy]
AllIceAllGen = df.loc[AllIce]
AllDraAllGen = df.loc[AllDra]
AllDarAllGen = df.loc[AllDar]
AllFaiAllGen = df.loc[AllFai]

# Gen 1
T1NorGen1 = df.loc[np.logical_and(T1Nor, Gen1)]
T1FigGen1 = df.loc[np.logical_and(T1Fig, Gen1)]
T1FlyGen1 = df.loc[np.logical_and(T1Fly, Gen1)]
T1PoiGen1 = df.loc[np.logical_and(T1Poi, Gen1)]
T1GroGen1 = df.loc[np.logical_and(T1Gro, Gen1)]
T1RocGen1 = df.loc[np.logical_and(T1Roc, Gen1)]
T1BugGen1 = df.loc[np.logical_and(T1Bug, Gen1)]
T1GhoGen1 = df.loc[np.logical_and(T1Gho, Gen1)]
T1SteGen1 = df.loc[np.logical_and(T1Ste, Gen1)]
T1FirGen1 = df.loc[np.logical_and(T1Fir, Gen1)]
T1WatGen1 = df.loc[np.logical_and(T1Wat, Gen1)]
T1GraGen1 = df.loc[np.logical_and(T1Gra, Gen1)]
T1EleGen1 = df.loc[np.logical_and(T1Ele, Gen1)]
T1PsyGen1 = df.loc[np.logical_and(T1Psy, Gen1)]
T1IceGen1 = df.loc[np.logical_and(T1Ice, Gen1)]
T1DraGen1 = df.loc[np.logical_and(T1Dra, Gen1)]
T1DarGen1 = df.loc[np.logical_and(T1Dar, Gen1)]
T1FaiGen1 = df.loc[np.logical_and(T1Fai, Gen1)]

T2NorGen1 = df.loc[np.logical_and(T2Nor, Gen1)]
T2FigGen1 = df.loc[np.logical_and(T2Fig, Gen1)]
T2FlyGen1 = df.loc[np.logical_and(T2Fly, Gen1)]
T2PoiGen1 = df.loc[np.logical_and(T2Poi, Gen1)]
T2GroGen1 = df.loc[np.logical_and(T2Gro, Gen1)]
T2RocGen1 = df.loc[np.logical_and(T2Roc, Gen1)]
T2BugGen1 = df.loc[np.logical_and(T2Bug, Gen1)]
T2GhoGen1 = df.loc[np.logical_and(T2Gho, Gen1)]
T2SteGen1 = df.loc[np.logical_and(T2Ste, Gen1)]
T2FirGen1 = df.loc[np.logical_and(T2Fir, Gen1)]
T2WatGen1 = df.loc[np.logical_and(T2Wat, Gen1)]
T2GraGen1 = df.loc[np.logical_and(T2Gra, Gen1)]
T2EleGen1 = df.loc[np.logical_and(T2Ele, Gen1)]
T2PsyGen1 = df.loc[np.logical_and(T2Psy, Gen1)]
T2IceGen1 = df.loc[np.logical_and(T2Ice, Gen1)]
T2DraGen1 = df.loc[np.logical_and(T2Dra, Gen1)]
T2DarGen1 = df.loc[np.logical_and(T2Dar, Gen1)]
T2FaiGen1 = df.loc[np.logical_and(T2Fai, Gen1)]

AllNorGen1 = df.loc[np.logical_and(AllNor, Gen1)]
AllFigGen1 = df.loc[np.logical_and(AllFig, Gen1)]
AllFlyGen1 = df.loc[np.logical_and(AllFly, Gen1)]
AllPoiGen1 = df.loc[np.logical_and(AllPoi, Gen1)]
AllGroGen1 = df.loc[np.logical_and(AllGro, Gen1)]
AllRocGen1 = df.loc[np.logical_and(AllRoc, Gen1)]
AllBugGen1 = df.loc[np.logical_and(AllBug, Gen1)]
AllGhoGen1 = df.loc[np.logical_and(AllGho, Gen1)]
AllSteGen1 = df.loc[np.logical_and(AllSte, Gen1)]
AllFirGen1 = df.loc[np.logical_and(AllFir, Gen1)]
AllWatGen1 = df.loc[np.logical_and(AllWat, Gen1)]
AllGraGen1 = df.loc[np.logical_and(AllGra, Gen1)]
AllEleGen1 = df.loc[np.logical_and(AllEle, Gen1)]
AllPsyGen1 = df.loc[np.logical_and(AllPsy, Gen1)]
AllIceGen1 = df.loc[np.logical_and(AllIce, Gen1)]
AllDraGen1 = df.loc[np.logical_and(AllDra, Gen1)]
AllDarGen1 = df.loc[np.logical_and(AllDar, Gen1)]
AllFaiGen1 = df.loc[np.logical_and(AllFai, Gen1)]

# Gen 2
T1NorGen2 = df.loc[np.logical_and(T1Nor, Gen2)]
T1FigGen2 = df.loc[np.logical_and(T1Fig, Gen2)]
T1FlyGen2 = df.loc[np.logical_and(T1Fly, Gen2)]
T1PoiGen2 = df.loc[np.logical_and(T1Poi, Gen2)]
T1GroGen2 = df.loc[np.logical_and(T1Gro, Gen2)]
T1RocGen2 = df.loc[np.logical_and(T1Roc, Gen2)]
T1BugGen2 = df.loc[np.logical_and(T1Bug, Gen2)]
T1GhoGen2 = df.loc[np.logical_and(T1Gho, Gen2)]
T1SteGen2 = df.loc[np.logical_and(T1Ste, Gen2)]
T1FirGen2 = df.loc[np.logical_and(T1Fir, Gen2)]
T1WatGen2 = df.loc[np.logical_and(T1Wat, Gen2)]
T1GraGen2 = df.loc[np.logical_and(T1Gra, Gen2)]
T1EleGen2 = df.loc[np.logical_and(T1Ele, Gen2)]
T1PsyGen2 = df.loc[np.logical_and(T1Psy, Gen2)]
T1IceGen2 = df.loc[np.logical_and(T1Ice, Gen2)]
T1DraGen2 = df.loc[np.logical_and(T1Dra, Gen2)]
T1DarGen2 = df.loc[np.logical_and(T1Dar, Gen2)]
T1FaiGen2 = df.loc[np.logical_and(T1Fai, Gen2)]

T2NorGen2 = df.loc[np.logical_and(T2Nor, Gen2)]
T2FigGen2 = df.loc[np.logical_and(T2Fig, Gen2)]
T2FlyGen2 = df.loc[np.logical_and(T2Fly, Gen2)]
T2PoiGen2 = df.loc[np.logical_and(T2Poi, Gen2)]
T2GroGen2 = df.loc[np.logical_and(T2Gro, Gen2)]
T2RocGen2 = df.loc[np.logical_and(T2Roc, Gen2)]
T2BugGen2 = df.loc[np.logical_and(T2Bug, Gen2)]
T2GhoGen2 = df.loc[np.logical_and(T2Gho, Gen2)]
T2SteGen2 = df.loc[np.logical_and(T2Ste, Gen2)]
T2FirGen2 = df.loc[np.logical_and(T2Fir, Gen2)]
T2WatGen2 = df.loc[np.logical_and(T2Wat, Gen2)]
T2GraGen2 = df.loc[np.logical_and(T2Gra, Gen2)]
T2EleGen2 = df.loc[np.logical_and(T2Ele, Gen2)]
T2PsyGen2 = df.loc[np.logical_and(T2Psy, Gen2)]
T2IceGen2 = df.loc[np.logical_and(T2Ice, Gen2)]
T2DraGen2 = df.loc[np.logical_and(T2Dra, Gen2)]
T2DarGen2 = df.loc[np.logical_and(T2Dar, Gen2)]
T2FaiGen2 = df.loc[np.logical_and(T2Fai, Gen2)]

AllNorGen2 = df.loc[np.logical_and(AllNor, Gen2)]
AllFigGen2 = df.loc[np.logical_and(AllFig, Gen2)]
AllFlyGen2 = df.loc[np.logical_and(AllFly, Gen2)]
AllPoiGen2 = df.loc[np.logical_and(AllPoi, Gen2)]
AllGroGen2 = df.loc[np.logical_and(AllGro, Gen2)]
AllRocGen2 = df.loc[np.logical_and(AllRoc, Gen2)]
AllBugGen2 = df.loc[np.logical_and(AllBug, Gen2)]
AllGhoGen2 = df.loc[np.logical_and(AllGho, Gen2)]
AllSteGen2 = df.loc[np.logical_and(AllSte, Gen2)]
AllFirGen2 = df.loc[np.logical_and(AllFir, Gen2)]
AllWatGen2 = df.loc[np.logical_and(AllWat, Gen2)]
AllGraGen2 = df.loc[np.logical_and(AllGra, Gen2)]
AllEleGen2 = df.loc[np.logical_and(AllEle, Gen2)]
AllPsyGen2 = df.loc[np.logical_and(AllPsy, Gen2)]
AllIceGen2 = df.loc[np.logical_and(AllIce, Gen2)]
AllDraGen2 = df.loc[np.logical_and(AllDra, Gen2)]
AllDarGen2 = df.loc[np.logical_and(AllDar, Gen2)]
AllFaiGen2 = df.loc[np.logical_and(AllFai, Gen2)]

# Gen 3
T1NorGen3 = df.loc[np.logical_and(T1Nor, Gen3)]
T1FigGen3 = df.loc[np.logical_and(T1Fig, Gen3)]
T1FlyGen3 = df.loc[np.logical_and(T1Fly, Gen3)]
T1PoiGen3 = df.loc[np.logical_and(T1Poi, Gen3)]
T1GroGen3 = df.loc[np.logical_and(T1Gro, Gen3)]
T1RocGen3 = df.loc[np.logical_and(T1Roc, Gen3)]
T1BugGen3 = df.loc[np.logical_and(T1Bug, Gen3)]
T1GhoGen3 = df.loc[np.logical_and(T1Gho, Gen3)]
T1SteGen3 = df.loc[np.logical_and(T1Ste, Gen3)]
T1FirGen3 = df.loc[np.logical_and(T1Fir, Gen3)]
T1WatGen3 = df.loc[np.logical_and(T1Wat, Gen3)]
T1GraGen3 = df.loc[np.logical_and(T1Gra, Gen3)]
T1EleGen3 = df.loc[np.logical_and(T1Ele, Gen3)]
T1PsyGen3 = df.loc[np.logical_and(T1Psy, Gen3)]
T1IceGen3 = df.loc[np.logical_and(T1Ice, Gen3)]
T1DraGen3 = df.loc[np.logical_and(T1Dra, Gen3)]
T1DarGen3 = df.loc[np.logical_and(T1Dar, Gen3)]
T1FaiGen3 = df.loc[np.logical_and(T1Fai, Gen3)]

T2NorGen3 = df.loc[np.logical_and(T2Nor, Gen3)]
T2FigGen3 = df.loc[np.logical_and(T2Fig, Gen3)]
T2FlyGen3 = df.loc[np.logical_and(T2Fly, Gen3)]
T2PoiGen3 = df.loc[np.logical_and(T2Poi, Gen3)]
T2GroGen3 = df.loc[np.logical_and(T2Gro, Gen3)]
T2RocGen3 = df.loc[np.logical_and(T2Roc, Gen3)]
T2BugGen3 = df.loc[np.logical_and(T2Bug, Gen3)]
T2GhoGen3 = df.loc[np.logical_and(T2Gho, Gen3)]
T2SteGen3 = df.loc[np.logical_and(T2Ste, Gen3)]
T2FirGen3 = df.loc[np.logical_and(T2Fir, Gen3)]
T2WatGen3 = df.loc[np.logical_and(T2Wat, Gen3)]
T2GraGen3 = df.loc[np.logical_and(T2Gra, Gen3)]
T2EleGen3 = df.loc[np.logical_and(T2Ele, Gen3)]
T2PsyGen3 = df.loc[np.logical_and(T2Psy, Gen3)]
T2IceGen3 = df.loc[np.logical_and(T2Ice, Gen3)]
T2DraGen3 = df.loc[np.logical_and(T2Dra, Gen3)]
T2DarGen3 = df.loc[np.logical_and(T2Dar, Gen3)]
T2FaiGen3 = df.loc[np.logical_and(T2Fai, Gen3)]

AllNorGen3 = df.loc[np.logical_and(AllNor, Gen3)]
AllFigGen3 = df.loc[np.logical_and(AllFig, Gen3)]
AllFlyGen3 = df.loc[np.logical_and(AllFly, Gen3)]
AllPoiGen3 = df.loc[np.logical_and(AllPoi, Gen3)]
AllGroGen3 = df.loc[np.logical_and(AllGro, Gen3)]
AllRocGen3 = df.loc[np.logical_and(AllRoc, Gen3)]
AllBugGen3 = df.loc[np.logical_and(AllBug, Gen3)]
AllGhoGen3 = df.loc[np.logical_and(AllGho, Gen3)]
AllSteGen3 = df.loc[np.logical_and(AllSte, Gen3)]
AllFirGen3 = df.loc[np.logical_and(AllFir, Gen3)]
AllWatGen3 = df.loc[np.logical_and(AllWat, Gen3)]
AllGraGen3 = df.loc[np.logical_and(AllGra, Gen3)]
AllEleGen3 = df.loc[np.logical_and(AllEle, Gen3)]
AllPsyGen3 = df.loc[np.logical_and(AllPsy, Gen3)]
AllIceGen3 = df.loc[np.logical_and(AllIce, Gen3)]
AllDraGen3 = df.loc[np.logical_and(AllDra, Gen3)]
AllDarGen3 = df.loc[np.logical_and(AllDar, Gen3)]
AllFaiGen3 = df.loc[np.logical_and(AllFai, Gen3)]

# Gen 4
T1NorGen4 = df.loc[np.logical_and(T1Nor, Gen4)]
T1FigGen4 = df.loc[np.logical_and(T1Fig, Gen4)]
T1FlyGen4 = df.loc[np.logical_and(T1Fly, Gen4)]
T1PoiGen4 = df.loc[np.logical_and(T1Poi, Gen4)]
T1GroGen4 = df.loc[np.logical_and(T1Gro, Gen4)]
T1RocGen4 = df.loc[np.logical_and(T1Roc, Gen4)]
T1BugGen4 = df.loc[np.logical_and(T1Bug, Gen4)]
T1GhoGen4 = df.loc[np.logical_and(T1Gho, Gen4)]
T1SteGen4 = df.loc[np.logical_and(T1Ste, Gen4)]
T1FirGen4 = df.loc[np.logical_and(T1Fir, Gen4)]
T1WatGen4 = df.loc[np.logical_and(T1Wat, Gen4)]
T1GraGen4 = df.loc[np.logical_and(T1Gra, Gen4)]
T1EleGen4 = df.loc[np.logical_and(T1Ele, Gen4)]
T1PsyGen4 = df.loc[np.logical_and(T1Psy, Gen4)]
T1IceGen4 = df.loc[np.logical_and(T1Ice, Gen4)]
T1DraGen4 = df.loc[np.logical_and(T1Dra, Gen4)]
T1DarGen4 = df.loc[np.logical_and(T1Dar, Gen4)]
T1FaiGen4 = df.loc[np.logical_and(T1Fai, Gen4)]

T2NorGen4 = df.loc[np.logical_and(T2Nor, Gen4)]
T2FigGen4 = df.loc[np.logical_and(T2Fig, Gen4)]
T2FlyGen4 = df.loc[np.logical_and(T2Fly, Gen4)]
T2PoiGen4 = df.loc[np.logical_and(T2Poi, Gen4)]
T2GroGen4 = df.loc[np.logical_and(T2Gro, Gen4)]
T2RocGen4 = df.loc[np.logical_and(T2Roc, Gen4)]
T2BugGen4 = df.loc[np.logical_and(T2Bug, Gen4)]
T2GhoGen4 = df.loc[np.logical_and(T2Gho, Gen4)]
T2SteGen4 = df.loc[np.logical_and(T2Ste, Gen4)]
T2FirGen4 = df.loc[np.logical_and(T2Fir, Gen4)]
T2WatGen4 = df.loc[np.logical_and(T2Wat, Gen4)]
T2GraGen4 = df.loc[np.logical_and(T2Gra, Gen4)]
T2EleGen4 = df.loc[np.logical_and(T2Ele, Gen4)]
T2PsyGen4 = df.loc[np.logical_and(T2Psy, Gen4)]
T2IceGen4 = df.loc[np.logical_and(T2Ice, Gen4)]
T2DraGen4 = df.loc[np.logical_and(T2Dra, Gen4)]
T2DarGen4 = df.loc[np.logical_and(T2Dar, Gen4)]
T2FaiGen4 = df.loc[np.logical_and(T2Fai, Gen4)]

AllNorGen4 = df.loc[np.logical_and(AllNor, Gen4)]
AllFigGen4 = df.loc[np.logical_and(AllFig, Gen4)]
AllFlyGen4 = df.loc[np.logical_and(AllFly, Gen4)]
AllPoiGen4 = df.loc[np.logical_and(AllPoi, Gen4)]
AllGroGen4 = df.loc[np.logical_and(AllGro, Gen4)]
AllRocGen4 = df.loc[np.logical_and(AllRoc, Gen4)]
AllBugGen4 = df.loc[np.logical_and(AllBug, Gen4)]
AllGhoGen4 = df.loc[np.logical_and(AllGho, Gen4)]
AllSteGen4 = df.loc[np.logical_and(AllSte, Gen4)]
AllFirGen4 = df.loc[np.logical_and(AllFir, Gen4)]
AllWatGen4 = df.loc[np.logical_and(AllWat, Gen4)]
AllGraGen4 = df.loc[np.logical_and(AllGra, Gen4)]
AllEleGen4 = df.loc[np.logical_and(AllEle, Gen4)]
AllPsyGen4 = df.loc[np.logical_and(AllPsy, Gen4)]
AllIceGen4 = df.loc[np.logical_and(AllIce, Gen4)]
AllDraGen4 = df.loc[np.logical_and(AllDra, Gen4)]
AllDarGen4 = df.loc[np.logical_and(AllDar, Gen4)]
AllFaiGen4 = df.loc[np.logical_and(AllFai, Gen4)]

# Gen 5
T1NorGen5 = df.loc[np.logical_and(T1Nor, Gen5)]
T1FigGen5 = df.loc[np.logical_and(T1Fig, Gen5)]
T1FlyGen5 = df.loc[np.logical_and(T1Fly, Gen5)]
T1PoiGen5 = df.loc[np.logical_and(T1Poi, Gen5)]
T1GroGen5 = df.loc[np.logical_and(T1Gro, Gen5)]
T1RocGen5 = df.loc[np.logical_and(T1Roc, Gen5)]
T1BugGen5 = df.loc[np.logical_and(T1Bug, Gen5)]
T1GhoGen5 = df.loc[np.logical_and(T1Gho, Gen5)]
T1SteGen5 = df.loc[np.logical_and(T1Ste, Gen5)]
T1FirGen5 = df.loc[np.logical_and(T1Fir, Gen5)]
T1WatGen5 = df.loc[np.logical_and(T1Wat, Gen5)]
T1GraGen5 = df.loc[np.logical_and(T1Gra, Gen5)]
T1EleGen5 = df.loc[np.logical_and(T1Ele, Gen5)]
T1PsyGen5 = df.loc[np.logical_and(T1Psy, Gen5)]
T1IceGen5 = df.loc[np.logical_and(T1Ice, Gen5)]
T1DraGen5 = df.loc[np.logical_and(T1Dra, Gen5)]
T1DarGen5 = df.loc[np.logical_and(T1Dar, Gen5)]
T1FaiGen5 = df.loc[np.logical_and(T1Fai, Gen5)]

T2NorGen5 = df.loc[np.logical_and(T2Nor, Gen5)]
T2FigGen5 = df.loc[np.logical_and(T2Fig, Gen5)]
T2FlyGen5 = df.loc[np.logical_and(T2Fly, Gen5)]
T2PoiGen5 = df.loc[np.logical_and(T2Poi, Gen5)]
T2GroGen5 = df.loc[np.logical_and(T2Gro, Gen5)]
T2RocGen5 = df.loc[np.logical_and(T2Roc, Gen5)]
T2BugGen5 = df.loc[np.logical_and(T2Bug, Gen5)]
T2GhoGen5 = df.loc[np.logical_and(T2Gho, Gen5)]
T2SteGen5 = df.loc[np.logical_and(T2Ste, Gen5)]
T2FirGen5 = df.loc[np.logical_and(T2Fir, Gen5)]
T2WatGen5 = df.loc[np.logical_and(T2Wat, Gen5)]
T2GraGen5 = df.loc[np.logical_and(T2Gra, Gen5)]
T2EleGen5 = df.loc[np.logical_and(T2Ele, Gen5)]
T2PsyGen5 = df.loc[np.logical_and(T2Psy, Gen5)]
T2IceGen5 = df.loc[np.logical_and(T2Ice, Gen5)]
T2DraGen5 = df.loc[np.logical_and(T2Dra, Gen5)]
T2DarGen5 = df.loc[np.logical_and(T2Dar, Gen5)]
T2FaiGen5 = df.loc[np.logical_and(T2Fai, Gen5)]

AllNorGen5 = df.loc[np.logical_and(AllNor, Gen5)]
AllFigGen5 = df.loc[np.logical_and(AllFig, Gen5)]
AllFlyGen5 = df.loc[np.logical_and(AllFly, Gen5)]
AllPoiGen5 = df.loc[np.logical_and(AllPoi, Gen5)]
AllGroGen5 = df.loc[np.logical_and(AllGro, Gen5)]
AllRocGen5 = df.loc[np.logical_and(AllRoc, Gen5)]
AllBugGen5 = df.loc[np.logical_and(AllBug, Gen5)]
AllGhoGen5 = df.loc[np.logical_and(AllGho, Gen5)]
AllSteGen5 = df.loc[np.logical_and(AllSte, Gen5)]
AllFirGen5 = df.loc[np.logical_and(AllFir, Gen5)]
AllWatGen5 = df.loc[np.logical_and(AllWat, Gen5)]
AllGraGen5 = df.loc[np.logical_and(AllGra, Gen5)]
AllEleGen5 = df.loc[np.logical_and(AllEle, Gen5)]
AllPsyGen5 = df.loc[np.logical_and(AllPsy, Gen5)]
AllIceGen5 = df.loc[np.logical_and(AllIce, Gen5)]
AllDraGen5 = df.loc[np.logical_and(AllDra, Gen5)]
AllDarGen5 = df.loc[np.logical_and(AllDar, Gen5)]
AllFaiGen5 = df.loc[np.logical_and(AllFai, Gen5)]

# Gen 6
T1NorGen6 = df.loc[np.logical_and(T1Nor, Gen6)]
T1FigGen6 = df.loc[np.logical_and(T1Fig, Gen6)]
T1FlyGen6 = df.loc[np.logical_and(T1Fly, Gen6)]
T1PoiGen6 = df.loc[np.logical_and(T1Poi, Gen6)]
T1GroGen6 = df.loc[np.logical_and(T1Gro, Gen6)]
T1RocGen6 = df.loc[np.logical_and(T1Roc, Gen6)]
T1BugGen6 = df.loc[np.logical_and(T1Bug, Gen6)]
T1GhoGen6 = df.loc[np.logical_and(T1Gho, Gen6)]
T1SteGen6 = df.loc[np.logical_and(T1Ste, Gen6)]
T1FirGen6 = df.loc[np.logical_and(T1Fir, Gen6)]
T1WatGen6 = df.loc[np.logical_and(T1Wat, Gen6)]
T1GraGen6 = df.loc[np.logical_and(T1Gra, Gen6)]
T1EleGen6 = df.loc[np.logical_and(T1Ele, Gen6)]
T1PsyGen6 = df.loc[np.logical_and(T1Psy, Gen6)]
T1IceGen6 = df.loc[np.logical_and(T1Ice, Gen6)]
T1DraGen6 = df.loc[np.logical_and(T1Dra, Gen6)]
T1DarGen6 = df.loc[np.logical_and(T1Dar, Gen6)]
T1FaiGen6 = df.loc[np.logical_and(T1Fai, Gen6)]

T2NorGen6 = df.loc[np.logical_and(T2Nor, Gen6)]
T2FigGen6 = df.loc[np.logical_and(T2Fig, Gen6)]
T2FlyGen6 = df.loc[np.logical_and(T2Fly, Gen6)]
T2PoiGen6 = df.loc[np.logical_and(T2Poi, Gen6)]
T2GroGen6 = df.loc[np.logical_and(T2Gro, Gen6)]
T2RocGen6 = df.loc[np.logical_and(T2Roc, Gen6)]
T2BugGen6 = df.loc[np.logical_and(T2Bug, Gen6)]
T2GhoGen6 = df.loc[np.logical_and(T2Gho, Gen6)]
T2SteGen6 = df.loc[np.logical_and(T2Ste, Gen6)]
T2FirGen6 = df.loc[np.logical_and(T2Fir, Gen6)]
T2WatGen6 = df.loc[np.logical_and(T2Wat, Gen6)]
T2GraGen6 = df.loc[np.logical_and(T2Gra, Gen6)]
T2EleGen6 = df.loc[np.logical_and(T2Ele, Gen6)]
T2PsyGen6 = df.loc[np.logical_and(T2Psy, Gen6)]
T2IceGen6 = df.loc[np.logical_and(T2Ice, Gen6)]
T2DraGen6 = df.loc[np.logical_and(T2Dra, Gen6)]
T2DarGen6 = df.loc[np.logical_and(T2Dar, Gen6)]
T2FaiGen6 = df.loc[np.logical_and(T2Fai, Gen6)]

AllNorGen6 = df.loc[np.logical_and(AllNor, Gen6)]
AllFigGen6 = df.loc[np.logical_and(AllFig, Gen6)]
AllFlyGen6 = df.loc[np.logical_and(AllFly, Gen6)]
AllPoiGen6 = df.loc[np.logical_and(AllPoi, Gen6)]
AllGroGen6 = df.loc[np.logical_and(AllGro, Gen6)]
AllRocGen6 = df.loc[np.logical_and(AllRoc, Gen6)]
AllBugGen6 = df.loc[np.logical_and(AllBug, Gen6)]
AllGhoGen6 = df.loc[np.logical_and(AllGho, Gen6)]
AllSteGen6 = df.loc[np.logical_and(AllSte, Gen6)]
AllFirGen6 = df.loc[np.logical_and(AllFir, Gen6)]
AllWatGen6 = df.loc[np.logical_and(AllWat, Gen6)]
AllGraGen6 = df.loc[np.logical_and(AllGra, Gen6)]
AllEleGen6 = df.loc[np.logical_and(AllEle, Gen6)]
AllPsyGen6 = df.loc[np.logical_and(AllPsy, Gen6)]
AllIceGen6 = df.loc[np.logical_and(AllIce, Gen6)]
AllDraGen6 = df.loc[np.logical_and(AllDra, Gen6)]
AllDarGen6 = df.loc[np.logical_and(AllDar, Gen6)]
AllFaiGen6 = df.loc[np.logical_and(AllFai, Gen6)]

########## Bar Plots

##### Listing the data

# All Generations
Y_T1AllGen = [len(T1NorAllGen), len(T1FigAllGen), len(T1FlyAllGen), len(T1PoiAllGen), len(T1GroAllGen), len(T1RocAllGen), len(T1BugAllGen), len(T1GhoAllGen), len(T1SteAllGen), len(T1FirAllGen), len(T1WatAllGen), len(T1GraAllGen), len(T1EleAllGen), len(T1PsyAllGen), len(T1IceAllGen), len(T1DraAllGen), len(T1DarAllGen), len(T1FaiAllGen)]
Y_T2AllGen = [len(T2NorAllGen), len(T2FigAllGen), len(T2FlyAllGen), len(T2PoiAllGen), len(T2GroAllGen), len(T2RocAllGen), len(T2BugAllGen), len(T2GhoAllGen), len(T2SteAllGen), len(T2FirAllGen), len(T2WatAllGen), len(T2GraAllGen), len(T2EleAllGen), len(T2PsyAllGen), len(T2IceAllGen), len(T2DraAllGen), len(T2DarAllGen), len(T2FaiAllGen)]
Y_AllAllGen = [len(AllNorAllGen), len(AllFigAllGen), len(AllFlyAllGen), len(AllPoiAllGen), len(AllGroAllGen), len(AllRocAllGen), len(AllBugAllGen), len(AllGhoAllGen), len(AllSteAllGen), len(AllFirAllGen), len(AllWatAllGen), len(AllGraAllGen), len(AllEleAllGen), len(AllPsyAllGen), len(AllIceAllGen), len(AllDraAllGen), len(AllDarAllGen), len(AllFaiAllGen)]

# Gen1
Y_T1Gen1 = [len(T1NorGen1), len(T1FigGen1), len(T1FlyGen1), len(T1PoiGen1), len(T1GroGen1), len(T1RocGen1), len(T1BugGen1), len(T1GhoGen1), len(T1SteGen1), len(T1FirGen1), len(T1WatGen1), len(T1GraGen1), len(T1EleGen1), len(T1PsyGen1), len(T1IceGen1), len(T1DraGen1), len(T1DarGen1), len(T1FaiGen1)]
Y_T2Gen1 = [len(T2NorGen1), len(T2FigGen1), len(T2FlyGen1), len(T2PoiGen1), len(T2GroGen1), len(T2RocGen1), len(T2BugGen1), len(T2GhoGen1), len(T2SteGen1), len(T2FirGen1), len(T2WatGen1), len(T2GraGen1), len(T2EleGen1), len(T2PsyGen1), len(T2IceGen1), len(T2DraGen1), len(T2DarGen1), len(T2FaiGen1)]
Y_AllGen1 = [len(AllNorGen1), len(AllFigGen1), len(AllFlyGen1), len(AllPoiGen1), len(AllGroGen1), len(AllRocGen1), len(AllBugGen1), len(AllGhoGen1), len(AllSteGen1), len(AllFirGen1), len(AllWatGen1), len(AllGraGen1), len(AllEleGen1), len(AllPsyGen1), len(AllIceGen1), len(AllDraGen1), len(AllDarGen1), len(AllFaiGen1)]

# Gen 2
Y_T1Gen2 = [len(T1NorGen2), len(T1FigGen2), len(T1FlyGen2), len(T1PoiGen2), len(T1GroGen2), len(T1RocGen2), len(T1BugGen2), len(T1GhoGen2), len(T1SteGen2), len(T1FirGen2), len(T1WatGen2), len(T1GraGen2), len(T1EleGen2), len(T1PsyGen2), len(T1IceGen2), len(T1DraGen2), len(T1DarGen2), len(T1FaiGen2)]
Y_T2Gen2 = [len(T2NorGen2), len(T2FigGen2), len(T2FlyGen2), len(T2PoiGen2), len(T2GroGen2), len(T2RocGen2), len(T2BugGen2), len(T2GhoGen2), len(T2SteGen2), len(T2FirGen2), len(T2WatGen2), len(T2GraGen2), len(T2EleGen2), len(T2PsyGen2), len(T2IceGen2), len(T2DraGen2), len(T2DarGen2), len(T2FaiGen2)]
Y_AllGen2 = [len(AllNorGen2), len(AllFigGen2), len(AllFlyGen2), len(AllPoiGen2), len(AllGroGen2), len(AllRocGen2), len(AllBugGen2), len(AllGhoGen2), len(AllSteGen2), len(AllFirGen2), len(AllWatGen2), len(AllGraGen2), len(AllEleGen2), len(AllPsyGen2), len(AllIceGen2), len(AllDraGen2), len(AllDarGen2), len(AllFaiGen2)]

# Gen 3
Y_T1Gen3 = [len(T1NorGen3), len(T1FigGen3), len(T1FlyGen3), len(T1PoiGen3), len(T1GroGen3), len(T1RocGen3), len(T1BugGen3), len(T1GhoGen3), len(T1SteGen3), len(T1FirGen3), len(T1WatGen3), len(T1GraGen3), len(T1EleGen3), len(T1PsyGen3), len(T1IceGen3), len(T1DraGen3), len(T1DarGen3), len(T1FaiGen3)]
Y_T2Gen3 = [len(T2NorGen3), len(T2FigGen3), len(T2FlyGen3), len(T2PoiGen3), len(T2GroGen3), len(T2RocGen3), len(T2BugGen3), len(T2GhoGen3), len(T2SteGen3), len(T2FirGen3), len(T2WatGen3), len(T2GraGen3), len(T2EleGen3), len(T2PsyGen3), len(T2IceGen3), len(T2DraGen3), len(T2DarGen3), len(T2FaiGen3)]
Y_AllGen3 = [len(AllNorGen3), len(AllFigGen3), len(AllFlyGen3), len(AllPoiGen3), len(AllGroGen3), len(AllRocGen3), len(AllBugGen3), len(AllGhoGen3), len(AllSteGen3), len(AllFirGen3), len(AllWatGen3), len(AllGraGen3), len(AllEleGen3), len(AllPsyGen3), len(AllIceGen3), len(AllDraGen3), len(AllDarGen3), len(AllFaiGen3)]

# Gen 4
Y_T1Gen4 = [len(T1NorGen4), len(T1FigGen4), len(T1FlyGen4), len(T1PoiGen4), len(T1GroGen4), len(T1RocGen4), len(T1BugGen4), len(T1GhoGen4), len(T1SteGen4), len(T1FirGen4), len(T1WatGen4), len(T1GraGen4), len(T1EleGen4), len(T1PsyGen4), len(T1IceGen4), len(T1DraGen4), len(T1DarGen4), len(T1FaiGen4)]
Y_T2Gen4 = [len(T2NorGen4), len(T2FigGen4), len(T2FlyGen4), len(T2PoiGen4), len(T2GroGen4), len(T2RocGen4), len(T2BugGen4), len(T2GhoGen4), len(T2SteGen4), len(T2FirGen4), len(T2WatGen4), len(T2GraGen4), len(T2EleGen4), len(T2PsyGen4), len(T2IceGen4), len(T2DraGen4), len(T2DarGen4), len(T2FaiGen4)]
Y_AllGen4 = [len(AllNorGen4), len(AllFigGen4), len(AllFlyGen4), len(AllPoiGen4), len(AllGroGen4), len(AllRocGen4), len(AllBugGen4), len(AllGhoGen4), len(AllSteGen4), len(AllFirGen4), len(AllWatGen4), len(AllGraGen4), len(AllEleGen4), len(AllPsyGen4), len(AllIceGen4), len(AllDraGen4), len(AllDarGen4), len(AllFaiGen4)]

# Gen 5
Y_T1Gen5 = [len(T1NorGen5), len(T1FigGen5), len(T1FlyGen5), len(T1PoiGen5), len(T1GroGen5), len(T1RocGen5), len(T1BugGen5), len(T1GhoGen5), len(T1SteGen5), len(T1FirGen5), len(T1WatGen5), len(T1GraGen5), len(T1EleGen5), len(T1PsyGen5), len(T1IceGen5), len(T1DraGen5), len(T1DarGen5), len(T1FaiGen5)]
Y_T2Gen5 = [len(T2NorGen5), len(T2FigGen5), len(T2FlyGen5), len(T2PoiGen5), len(T2GroGen5), len(T2RocGen5), len(T2BugGen5), len(T2GhoGen5), len(T2SteGen5), len(T2FirGen5), len(T2WatGen5), len(T2GraGen5), len(T2EleGen5), len(T2PsyGen5), len(T2IceGen5), len(T2DraGen5), len(T2DarGen5), len(T2FaiGen5)]
Y_AllGen5 = [len(AllNorGen5), len(AllFigGen5), len(AllFlyGen5), len(AllPoiGen5), len(AllGroGen5), len(AllRocGen5), len(AllBugGen5), len(AllGhoGen5), len(AllSteGen5), len(AllFirGen5), len(AllWatGen5), len(AllGraGen5), len(AllEleGen5), len(AllPsyGen5), len(AllIceGen5), len(AllDraGen5), len(AllDarGen5), len(AllFaiGen5)]

# Gen 6
Y_T1Gen6 = [len(T1NorGen6), len(T1FigGen6), len(T1FlyGen6), len(T1PoiGen6), len(T1GroGen6), len(T1RocGen6), len(T1BugGen6), len(T1GhoGen6), len(T1SteGen6), len(T1FirGen6), len(T1WatGen6), len(T1GraGen6), len(T1EleGen6), len(T1PsyGen6), len(T1IceGen6), len(T1DraGen6), len(T1DarGen6), len(T1FaiGen6)]
Y_T2Gen6 = [len(T2NorGen6), len(T2FigGen6), len(T2FlyGen6), len(T2PoiGen6), len(T2GroGen6), len(T2RocGen6), len(T2BugGen6), len(T2GhoGen6), len(T2SteGen6), len(T2FirGen6), len(T2WatGen6), len(T2GraGen6), len(T2EleGen6), len(T2PsyGen6), len(T2IceGen6), len(T2DraGen6), len(T2DarGen6), len(T2FaiGen6)]
Y_AllGen6 = [len(AllNorGen6), len(AllFigGen6), len(AllFlyGen6), len(AllPoiGen6), len(AllGroGen6), len(AllRocGen6), len(AllBugGen6), len(AllGhoGen6), len(AllSteGen6), len(AllFirGen6), len(AllWatGen6), len(AllGraGen6), len(AllEleGen6), len(AllPsyGen6), len(AllIceGen6), len(AllDraGen6), len(AllDarGen6), len(AllFaiGen6)]

X = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"]

Colours = {"Normal":"#A8A77A", "Fighting":"#C22E28", "Flying":"#A98FF3", "Poison":"#A33EA1", "Ground":"#E2BF65", "Rock":"#B6A136", "Bug":"#A6B91A", "Ghost":"#735797", "Steel":"#B7B7CE", "Fire":"#EE8130", "Water":"#6390F0", "Grass":"#7AC74C", "Electric":"#F7D02C", "Psychic":"#F95587", "Ice":"#96D9D6", "Dragon":"#6F35FC", "Dark":"#705746", "Fairy":"#D685AD"}
COLORS = [Colours["Normal"], Colours["Fighting"], Colours["Flying"], Colours["Poison"], Colours["Ground"], Colours["Rock"], Colours["Bug"], Colours["Ghost"], Colours["Steel"], Colours["Fire"], Colours["Water"], Colours["Grass"], Colours["Electric"], Colours["Psychic"], Colours["Ice"], Colours["Dragon"], Colours["Dark"], Colours["Fairy"]]

width = 1/3

##### Plotting

# Type 1, All Gen
plt.figure(1)
ax = plt.subplot()
BarPltT1AllGen = ax.bar(X, Y_T1AllGen, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 1 Distribution, all Generations")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 150])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT1AllGen, ax)

# Type 2, All Gen
plt.figure(2)
ax = plt.subplot()
BarPltT2AllGen = ax.bar(X, Y_T2AllGen, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 2 Distribution, all Generations")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 150])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT2AllGen, ax)

# All Type, All Gen
plt.figure(3)
ax = plt.subplot()
BarPltAllAllGen = ax.bar(X, Y_AllAllGen, width, color = COLORS, zorder=2)

plt.title("Pokémon Type Distribution, all Generations")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 150])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltAllAllGen, ax)

#####

# Type 1, Gen 1
plt.figure(4)
ax = plt.subplot()
BarPltT1Gen1 = ax.bar(X, Y_T1Gen1, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 1 Distribution, Generation 1")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT1Gen1, ax)

# Type 2, Gen 1
plt.figure(5)
ax = plt.subplot()
BarPltT2Gen1 = ax.bar(X, Y_T2Gen1, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 2 Distribution, Generation 1")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT2Gen1, ax)

# All Type, Gen 1
plt.figure(6)
ax = plt.subplot()
BarPltAllGen1 = ax.bar(X, Y_AllGen1, width, color = COLORS, zorder=2)

plt.title("Pokémon Type Distribution, Generation 1")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltAllGen1, ax)

#####

# Type 1, Gen 2
plt.figure(7)
ax = plt.subplot()
BarPltT1Gen2 = ax.bar(X, Y_T1Gen2, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 1 Distribution, Generation 2")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT1Gen2, ax)

# Type 2, Gen 2
plt.figure(8)
ax = plt.subplot()
BarPltT2Gen2 = ax.bar(X, Y_T2Gen2, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 2 Distribution, Generation 2")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT2Gen2, ax)

# All Type, Gen 2
plt.figure(9)
ax = plt.subplot()
BarPltAllGen2 = ax.bar(X, Y_AllGen2, width, color = COLORS, zorder=2)

plt.title("Pokémon Type Distribution, Generation 2")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltAllGen2, ax)

#####

# Type 1, Gen 3
plt.figure(10)
ax = plt.subplot()
BarPltT1Gen3 = ax.bar(X, Y_T1Gen3, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 1 Distribution, Generation 3")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT1Gen3, ax)

# Type 2, Gen 3
plt.figure(11)
ax = plt.subplot()
BarPltT2Gen3 = ax.bar(X, Y_T2Gen3, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 2 Distribution, Generation 3")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT2Gen3, ax)

# All Type, Gen 3
plt.figure(12)
ax = plt.subplot()
BarPltAllGen3 = ax.bar(X, Y_AllGen3, width, color = COLORS, zorder=2)

plt.title("Pokémon Type Distribution, Generation 3")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltAllGen3, ax)

#####

# Type 1, Gen 4
plt.figure(13)
ax = plt.subplot()
BarPltT1Gen4 = ax.bar(X, Y_T1Gen4, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 1 Distribution, Generation 4")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT1Gen4, ax)

# Type 2, Gen 4
plt.figure(14)
ax = plt.subplot()
BarPltT2Gen4 = ax.bar(X, Y_T2Gen4, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 2 Distribution, Generation 4")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT2Gen4, ax)

# All Type, Gen 4
plt.figure(15)
ax = plt.subplot()
BarPltAllGen4 = ax.bar(X, Y_AllGen4, width, color = COLORS, zorder=2)

plt.title("Pokémon Type Distribution, Generation 4")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltAllGen4, ax)

#####

# Type 1, Gen 5
plt.figure(16)
ax = plt.subplot()
BarPltT1Gen5 = ax.bar(X, Y_T1Gen5, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 1 Distribution, Generation 5")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT1Gen5, ax)

# Type 2, Gen 5
plt.figure(17)
ax = plt.subplot()
BarPltT2Gen5 = ax.bar(X, Y_T2Gen5, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 2 Distribution, Generation 5")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT2Gen5, ax)

# All Type, Gen 5
plt.figure(18)
ax = plt.subplot()
BarPltAllGen5 = ax.bar(X, Y_AllGen5, width, color = COLORS, zorder=2)

plt.title("Pokémon Type Distribution, Generation 5")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltAllGen5, ax)

#####

# Type 1, Gen 6
plt.figure(19)
ax = plt.subplot()
BarPltT1Gen6 = ax.bar(X, Y_T1Gen6, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 1 Distribution, Generation 6")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT1Gen6, ax)

# Type 2, Gen 6
plt.figure(20)
ax = plt.subplot()
BarPltT2Gen6 = ax.bar(X, Y_T2Gen6, width, color = COLORS, zorder=2)

plt.title("Pokémon Type 2 Distribution, Generation 6")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltT2Gen6, ax)

# All Type, Gen 6
plt.figure(21)
ax = plt.subplot()
BarPltAllGen6 = ax.bar(X, Y_AllGen6, width, color = COLORS, zorder=2)

plt.title("Pokémon Type Distribution, Generation 6")
plt.xlabel("Type")
plt.ylabel("Number of Pokémon")
plt.xticks(rotation="vertical")
plt.grid(linestyle="-", linewidth=0.25, zorder=0)
plt.ylim([0, 50])

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.025)

        ax.text(rect.get_x() + rect.get_width()/2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(BarPltAllGen6, ax)

plt.show()