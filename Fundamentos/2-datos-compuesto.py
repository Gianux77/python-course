lista = ["lucas dalto", "soy dalto", True,1.85]
print(lista)

#_indice = posicion, ej: 0,1,2,3
#_elemento = valor, ej: "lucas dalto"

print(lista[2])

# tuplas: son igual  a ala lista pero usamos corchetes ()

tupla = ("lucas dalto", "soy dalto", True,1.85)
print(tupla[3])
# las tuplas no se pueden modificar, las lista si

#creando un conjunto (set)
conjunto = {"lucas dalto", "soy dalto", True,1.85}
print(conjunto)
# cada elemento no podemos modificar
# no te muestra el indice
# no se puede poner mas elementos duplicados ni tanpoco nuevos

#CREANDO UN DICCIONARIO (dict)

diccionario = {
    'nombre':"lucas dalto",
    'canal' : "soy dalto",
    'esta_emocionado': True,
    'altura' : 1.84,
    'dato_duplicado' : "soy dalto"
}

print(diccionario['canal'])
print(diccionario['altura'])
print(diccionario['nombre'])





