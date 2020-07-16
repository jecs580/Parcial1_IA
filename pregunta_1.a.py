import math
import csv
datos=[]
def alumnos():
    with open('alumno.csv',newline='') as csvFile:
        alumno_reader=csv.reader(csvFile)
        next(alumno_reader)
        datos=[]
        for line in alumno_reader:
            datos.append(line)
    return datos

def media(datos,column):
    """Calculo para la media"""
    media=0
    count=0
    for i in datos:
        if i[column]!='':
            count+=1
            media+=int(i[column])
    media=media/count

    return media

def desv_estantar(datos,column):
    """Calculo para la desviacion estandar"""
    var=sum([((int(i[column])-media(datos,column))**2) for i in datos])
    var=var/(len(datos)-1)
    desv=math.sqrt(var)
    return desv

def desv_estantar1(datos,column):
    """Calculo para la desviacion estandar"""
    var=0
    count=0
    for i in datos:
        if i[column]!='':
            var+=(int(i[column])-media(datos,column))**2
            count+=1
    var=var/(count-1)
    desv=math.sqrt(var)
    return desv

datos=alumnos()
media_nota,media_edad=round(media(datos,4),2), round(media(datos,5),2)
desv_nota,desv_edad=round(desv_estantar1(datos,4),2), round(desv_estantar1(datos,5),2)

print("Pregunta 1.a: Obtenga la media y la desviacion estandar y explique que significa en cada caso mediante python sin uso de librerias\n")
print("LISTADO DE LOS DATOS")
print(datos)
print("\nEXPLICACION")
print("******* Analisis de la columna NOTA_PROMEDIO *******")
print(f"-Media de notas: {media_nota}")
print(f"-Desviacion estandar de: {desv_nota}")
print(f"Concluimos que la nota de un estudiante esta en promedio de: {media_nota}, con una desviacion estandar de: {desv_nota} que causa una tendencia a variar por debajo o encima del valor de la media.")
print("\n******* Analisis de la columna EDAD *******")
print(f"-Media de notas: {media_edad}")
print(f"-Desviacion estandar de: {desv_edad}")
print(f"Concluimos que la edad promedio de los estudiantes es de: {media_edad},  con una desviacion estandar de: {desv_edad} que causa con una tendencia a variar por debajo o encima del valor de la media.")