import pandas as pd
import numpy as np
import statistics as stats

print("Pregunta 1.b: Obtenga la media, la moda, la desviación estándar con el uso de numpy y pandas")
dataframe=pd.read_csv("./alumno.csv" ,sep=",")
print("LISTADO DE LOS DATOS")
print(dataframe)
media_nota=round(dataframe['nota_promedio'].mean(),2)
media_edad=round(dataframe['edad'].mean(),2)
print("\nMEDIA")
print(f"-Media de notas: {media_nota}")
print(f"-Media de edad: {media_edad}")

notas=np.asanyarray(dataframe['nota_promedio'])
edades=np.asanyarray(dataframe['edad'])
moda_nota=stats.mode(notas)
moda_edad=stats.mode(edades)
print("\nMODA")
print(f"-Moda de notas: {moda_nota}")
print(f"-Moda de edades: {moda_edad}")

desv_nota=round(dataframe['nota_promedio'].std(),2)
desv_edad= round(dataframe['edad'].std(),2)
print("\nDESVIACION ESTANDAR")
print(f"-Desviacion estandar de notas: {desv_nota}")
print(f"-Desviacion estandar de edad: {desv_edad}")