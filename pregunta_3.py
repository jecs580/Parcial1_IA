from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd

dataframe=pd.read_csv("./preprocesamiento_alumno_python.csv" ,sep=",")

# Cambiamos los valores de departamento a valores numericos
dataframe['departamento'].replace(['LP','CBBA','SC'],[0,1,2],inplace=True)
print(dataframe)
# Separamos los datos de la columna 'sexo' para la prediccion
X=np.array(dataframe.drop(['sexo'],1))
Y=np.array(dataframe['sexo'])

modeltree=DecisionTreeClassifier()

modeltree.fit(X,Y)
Y_pred=modeltree.predict([[ 0.,56.,23.], [0.,65.,23.66666667],[ 0.,87.,20.]])
print(Y_pred)