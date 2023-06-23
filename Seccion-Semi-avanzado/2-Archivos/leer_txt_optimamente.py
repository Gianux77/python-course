#abriendo el archivo con with open
with open("Seccion-Semi-avanzado\\2-Archivos\\texto_de_frank.txt") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
    #no es necesario cerrarlo al usar el with open
    