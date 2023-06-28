import pandas as pd

#usando la funcion pd.read_csv para leer un archivo CSV
df = pd.read_csv("Seccion-Semi-avanzado\\2-Archivos\\datos.csv")
df2 = pd.read_csv("Seccion-Semi-avanzado\\2-Archivos\\datos.csv") 
#obteniendo los nombres de la columnas nombre
nombres = df["nombre"]

# print(df)

"""
En Python, "slicing" se refiere a la técnica utilizada para extraer partes específicas de una secuencia, como una lista, una cadena o una tupla. 

El slicing se realiza utilizando la sintaxis de corchetes cuadrados [ ] y dos puntos :.

La sintaxis general del slicing es la siguiente:

secuencia[inicio:fin:paso]


Donde:

inicio : es el índice donde se inicia la porción que deseas extraer (inclusive).
fin: es el índice donde se detiene la extracción (exclusivo).
paso: (opcional) es el tamaño del salto entre los elementos seleccionados.
Es importante tener en cuenta que el índice inicio es inclusivo, lo que significa que el elemento en esa posición también se incluirá en el resultado. 
Por otro lado, el índice fin es exclusivo, lo que significa que el elemento en esa posición no se incluirá en el resultado.

"""
"""
cadena = "0123456789"

print(cadena[2:9])

"""
# ordedenando df por edad
df_orden_ascedente = df.sort_values("edad")
#print(df_orden_ascedente)

# ordenando df por edad pero de forma decendente
df_orden_decendente = df.sort_values("edad",ascending=False)
#print(df_orden_decendente)

#concantenando  los 2 dataframes
df_concatenado = pd.concat([df,df2])
# print(df_concatenado)

# la función head() se utiliza para mostrar las primeras filas de un DataFrame.
primer_fila = df.head(3) # muestra las primeras 3 filas
#print(primer_fila)

# la funcion tail() muestra las últimas filas del DataFrame por defecto
ultima_fila = df.tail(3)
# print(ultima_fila)

# accediendo a la cantidad de filas y columnas con shape
# shape se utiliza para obtener la forma
# o dimensiones de una estructura de datos multidimensional, como un arreglo NumPy o un DataFrame de Pandas.

filas_columnas_totales = df.shape
#print(filas_columnas_totales)

# obteniendo data estadistica del dataframe
df_info = df.describe()
#print(df_info)

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2,"edad"]
print(elemento_especifico_loc)

#accediendo a un elemento especifico del df con iloc
elemento_especifico_iloc = df.iloc[2,2]
print(elemento_especifico_iloc)
