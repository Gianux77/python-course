import csv


with open("Seccion-Semi-avanzado\\2-Archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row) 