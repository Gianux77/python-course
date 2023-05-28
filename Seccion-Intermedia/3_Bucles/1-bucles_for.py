#
#  animales = ["perro","gato","loro","cocodrilo"]
#
#   for animal in animales:
#       print(animal)
#   

animales = ["gato","perro","loro","cocodrilo","pez"] 

for animal in animales :
    print(f'Ahora la variable animal es igual a: {animal}')


#recorriendo la lista de numeros
numeros = [2,4,8,12,16]

for numero in numeros:
    resultado = numero * 2
    print(resultado)  
    
# iterar 2 lista al mismo tiempo, ¿ como lo hacemos ?

for numero, animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
# iterar lista por rango
for num in range(5,10):
    print(num)
    
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor  = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
# usando el else

for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print("el bucle termino")
    
    #Funciona apra iterar tuplas  y conjuntos.
