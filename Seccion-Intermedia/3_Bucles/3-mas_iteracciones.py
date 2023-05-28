frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Dalto"
numeros = [2,5,8,10]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue                         #que continue el codigo e ignore el valor que definimos
    print(f'me voy a comer una {fruta}')
    

#evitar que el bucle siga ejecutandose ( el else no se ejecuta cuando hay un break)
for fruta in frutas:
    print(f'me voy a comer una {fruta}')
    if fruta == 'pera':
        break              # finaliza el bucle
else:
    print("bucle terminado")
    
# recorrer una cadena de texto

for letra in cadena:
    print(letra)
    
# for en una linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)