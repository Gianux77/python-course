import pandas as pd

#usando la funcion pd.read_csv para leer un archivo CSV
df = pd.read_csv("Seccion-Semi-avanzado\\2-Archivos\\datos.csv")

#obteniendo los nombres de la columnas nombre
nombres = df["nombre"]

print(nombres)


