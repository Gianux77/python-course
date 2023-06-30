#cambiar el tipo de datos de una columnas
import pandas as pd
df = pd.read_csv("Seccion-Semi-avanzado\\2-Archivos\\datos.csv")
# print(df)

#convertir a string los datos de una columnas
# df["edad"] = df["edad"].astype(str)
# print(df["edad"]) 

#reemplazando los datos "hijo de odin" por "odin".
df["apellido"].replace("hijo de odin","odin",inplace=True)
#print(df["apellido"])
#print(df)

#eliminando las filas con datos vacios
df = df.dropna()                                 #con axis= 1 : eliminamos columnas
print(df)

"""
eliminando las filas repetidas:
df = df.drop_duplicates()

""" 
# creando el archivo CSV con el dateframe resultante (limpio)
df.to_csv("Seccion-Semi-avanzado\\3-Trabajando_con_Archivos\\datos_limpios.csv")