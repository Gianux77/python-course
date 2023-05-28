#cambiando sus posiciones de los parametros

def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase(adjetivo= "capo", nombre="Gian",apellido="Giupponi")
print(frase_resultante)

#creando una funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo="Tonto"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante2 = frase("Frank","Giupponi","Genio")
print(frase_resultante2)