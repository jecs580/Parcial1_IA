import pandas as pd
import numpy as np

print("Pregunta 2: Del archivo del problema 1 en WEKA y PYTHON realice el preprocesamiento utilizando al menos dos métodos del mismo.")

dataframe=pd.read_csv("./alumno.csv" ,sep=",")
print("LISTADO DE LOS DATOS")
print(dataframe.columns.values)
print(dataframe.values)

# nRemplazando los valores de la columna sexo a valores numeros de [0,1]
print("\nRemplazando de los valores de la columna sexo a valores numeros de [0,1]:")
dataframe['sexo'].replace(['M','F'],[0,1],inplace=True)
print(dataframe.values)

# Remplazando los valores faltantes en las columnas de nota_promedio y edad por la media de sus respectivas columnas
media_nota=dataframe['nota_promedio'].mean()
media_edad=dataframe['edad'].mean()
dataframe['nota_promedio']=dataframe['nota_promedio'].replace(np.nan,media_nota)
dataframe['edad']=dataframe['edad'].replace(np.nan,media_edad)
print("\nRemplazando de los valores faltantes en las columnas de nota_promedio y edad por la media de sus respectivas columnas:")
print(dataframe.values)

# Eliminando las columnas de CI y Nombre
print("\nEliminando las columnas de [CI,Nombre] y guardando los datos en un nuevo archivo llamado 'preprocesamiento_alumno_python.csv'")
dataframe.drop(['ci'],axis=1,inplace=True)
dataframe.drop(['nombre'],axis=1,inplace=True)
print(dataframe.columns.values)
print(dataframe.values)
dataframe.to_csv('preprocesamiento_alumno_python.csv',index = False)

