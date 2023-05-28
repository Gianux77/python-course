#CREANDO DICCIONARIO CON dict()
diccionario = dict(nombre="lucas",apellido="Dalto")


#la lista no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio"]): "jajaj"}

#creando diccionario con fromkeys() por defecto
diccionario = dict.fromkeys(["nombre","apellido"]) 

#creando diccionario con fromkeys() con 2 parametros
diccionario2 = dict.fromkeys(["nombre","apellido"], "No_se")



print(diccionario)
print(diccionario2) 
