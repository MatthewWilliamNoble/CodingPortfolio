from sklearn import tree
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

import numpy as np
import pandas as pd

#####

# Creating the pandas data frame
Path = r"C:\Users\Matthew\Documents\Pycharm\DataScienceProjects\Pokemon\PokemonData.csv"
df = pd.read_csv(Path, index_col=0)

# Data
X = df[["Total", "hasGender"]]

# Labels, Y
Y = df[["isLegendary"]]

# Classifiers -- using the default hyper-parameters
CLF_Tree = tree.DecisionTreeClassifier()
CLF_Perceptron = Perceptron()
CLF_KNN = KNeighborsClassifier()
CLF_Gauss = GaussianNB()

# Training the models on our data set X given Y labels
CLF_Tree.fit(X, Y)
CLF_Perceptron.fit(X, Y)
CLF_KNN.fit(X, Y)
CLF_Gauss.fit(X, Y)

# Testing the models using the same data X
Prediction_Tree = CLF_Tree.predict(X)
Accuracy_Tree = accuracy_score(Y, Prediction_Tree) * 100
print('Accuracy for DecisionTree: {}'.format(Accuracy_Tree))

Prediction_Perceptron = CLF_Perceptron.predict(X)
Accuracy_Perceptron = accuracy_score(Y, Prediction_Perceptron) * 100
print('Accuracy for Perceptron: {}'.format(Accuracy_Perceptron))

Prediction_KNN = CLF_KNN.predict(X)
Accuracy_KNN = accuracy_score(Y, Prediction_KNN) * 100
print('Accuracy for KNN: {}'.format(Accuracy_KNN))

Prediction_Gauss = CLF_Gauss.predict(X)
Accuracy_Gauss = accuracy_score(Y, Prediction_Gauss) * 100
print('Accuracy for Gauss: {}'.format(Accuracy_Gauss))

# Labelling the best classifier
index = np.argmax([Accuracy_Tree, Accuracy_Perceptron, Accuracy_KNN, Accuracy_Gauss])
classifiers = {0: "Decision Tree", 1:"Perceptron", 2: 'KNN', 3: "Gauss"}
print(" The best Legendary classifier is therefore {}".format(classifiers[index]))

#####

# Testing with Gen7 Pokémon
X1 = [[680, False]]  # Solgaleo  -- Legendary, Strong, Genderless
X2 = [[600, True]]   # Kommo-o   -- Non-legendary, Strong, Gendered
X3 = [[570, False]]  # Tapu-Koko -- Legendary, kinda-Strong, Genderless
X4 = [[490, True]]   # Oranguru  -- Non-Legendary, weak, Gendered

XList = [X1, X2, X3, X4]

for testcase in XList:
    R1 = CLF_Tree.predict(testcase)
    R2 = CLF_Perceptron.predict(testcase)
    R3 = CLF_KNN.predict(testcase)
    R4 = CLF_Gauss.predict(testcase)

    print(R1, R2, R3, R4)