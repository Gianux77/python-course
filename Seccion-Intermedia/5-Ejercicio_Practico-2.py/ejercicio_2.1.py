# FALTO EL PROFE  Y LOS PIBES ARMAN LAS CLASES.

#decir el nombre y la edad de los compañeros que vinieron hoy

# compañero = []
#  for i in range(7):
#    nombre= input("ingrese el nombre del compañero")
#    edad= int(input("ingrese la edad del compañero"))
#    compañero = (nombre,edad)
#    compañero.append(compañero)
#
# lo hacemos con unaq funcion mas facil

def obtener_compañeros(cantidad_de_compañeros):
    # creando la lista para los compañeros
    compañeros = []
    
    #ejecutando for para pedir al informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        #agregando la informacion a lista
        compañeros.append(compañero)
    
    #ordenando de menor a mayor segun la edad de los compañeros    
    compañeros.sort(key=lambda x:x[1]) # sort: ordena la tupla, con el segundo valor 1 que seria la edad
    
    #compañeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    #para definir al asistente y al profesor.
    asistente= compañeros[0][0]
    profesor= compañeros[-1][0]
    
    #returnamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna una funcion
asistente,profesor = obtener_compañeros(5)

#mostramos el resultado
print(f"El profesor es: {profesor} y su asistente es {asistente}")