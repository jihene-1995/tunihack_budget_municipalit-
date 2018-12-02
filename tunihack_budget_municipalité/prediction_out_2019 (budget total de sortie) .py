#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.ExcelFile('./scraping_file_ariana.xlsx')
df = pd.read_excel(data)
df.head()
X = df.iloc[0:len(df),0]
Y = df.iloc[0:len(df),2]
axes = plt.axes()
# dessiner une grille pour une meilleur lisibilité du graphe
axes.grid() 
# X et Y sont les variables qu'on a extraite dans le paragraphe précédent
plt.scatter(X,Y) 
plt.show()
#linregress() renvoie plusieurs variables de retour. On s'interessera 
# particulierement au slope et intercept
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
def predict(x):
    return slope * x + intercept
#la variable fitLine sera un tableau de valeurs prédites depuis la tableau de variables X
fitLine = predict(X)
plt.plot(X, fitLine, c='r')
print(predict(2019))
fichier = open("prediction.txt", "a")
fichier.write(str(predict(2019)))
fichier.close()
