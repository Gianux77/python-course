# keys: devuelve las claves
diccionario = {
    "nombre": 'lucas',
    "apellido": 'dalto',
    "subs": 1000000
}

claves =  diccionario.keys()

print(claves)

# get: nos devuelve el valor
clave1 = diccionario.get("nombre")
print(clave1)

# clear: elimina todos los elementos de la lista
# diccionario.clear()
# print(diccionario)

# eliminando un elemento del diccionario
diccionario.pop("subs") # en este caso elimina el contenido de subs
print(diccionario)

# items : para iterar el dict
# obteniendo un elemento dict_items iterable

diccionario_iterable = diccionario.items()
print(diccionario_iterable)