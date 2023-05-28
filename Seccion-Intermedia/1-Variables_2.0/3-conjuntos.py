#creando un conjunto con set()
conjunto = set(["Dato1"])

# metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"]) #frozenset son conjuntos congelados es para añadir a otro conjunto
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)

#Teorias de conjuntos
conjunto_A = {1,3,5,7}
conjunto_B = {1,3,7}

resultado = conjunto_B.issubset(conjunto_A)       # issubset = es para saber si un conjuntos es subconjunto de otro
print(resultado)                                 

#otra forma de saber
resultado2 = conjunto_B <= conjunto_A
print(resultado2)

#verificamos si es superconjuntos
resultado3 = conjunto_B.issuperset(conjunto_A)
resultado4 = conjunto_B > conjunto_A
print(resultado3)
print(resultado4)

#verificamos si hay un numero en comun
resultado5 = conjunto_B.isdisjoint(conjunto_A)  # cuando no hay un numero en comun o es distinto nos devuelve true.
print(resultado5)

