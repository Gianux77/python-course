
# le pedimos al ususario que nos digas una frase ( o varias )
frase = input("Decime una frase y te calculo cuanto tardarias si tuviera que decirla:  ")

# creamos un lista con todas las palabras que nos dio el usuario(separa en cuando hay un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len para ver cuantos elementos hay en una lista
cantidad_de_palabras = len(palabras_separadas)

#en caso que atrde mas de 1 minuto decircelo al usuario
if cantidad_de_palabras > 120:
    print("para flaco tampoco te pedi un testamento")
    
#calculamos cuanto tardaria en decir las palabras
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundo en decirlo')

print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 *1.3 /100} segundo en decirlo')


