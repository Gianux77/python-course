archivo = open("Seccion-Semi-avanzado\\2-Archivos\\texto_de_frank.txt") # open = abrir

# leer archivo completo
archivo2 = archivo.read()
# print(archivo)

#leer linea por linea y retorna ene una lista
lineas = archivo.readlines() 
#print(lineas)

#leer una sola linea
linea = archivo.readline()
print(linea)

#cerrar el archivo
archivo.close()    

print(archivo2)  