# list: crea una lista
lista = list(["hola","dalto",34])

print(lista)

# len: cuenta la cantidad de un elemento de una lista
resultado = len(lista)
print(resultado)

# append: agregando un elemento a la lista
lista.append("jajaja")
print(lista)

# insert: agregando un elemento a la lista de un indice especificado
lista.insert(2, "TOMA MATE") #2: muestra la posicion que quiero colocarle
print(lista)

# extend: agregando varios elementos a la lista
lista.extend([False,2030]) # para pasar varios elementos si o si le ponemos corchetes
print(lista)

# ELIMINANDO O REMOVIENDO  ELEMENTOS

# pop: eliminando un elemento de la lista (por su indice)
lista.pop(3) #-1 para eliminar el ultimo elemento de la lista
print(lista)

# remove: removiendo un elemento de la lista por su valor
lista.remove("TOMA MATE")
print(lista)


# clear: elimina todos los elementos de una lista
# lista.clear()

# ORDENA POSICION DE UNA LISTA
# solo para lista que contenga elementos int

lista2 = list([False,False,True,34,33,30,11])

# sort: ordena la lista( reverse = lo ordena en reversa)
lista2.sort()
print(lista2)

lista2.reverse()
print(lista2)

# index: verifica si un elemento se encuentra en una lista
elemnto_encontrado = lista2.index(True)
print(elemnto_encontrado)



