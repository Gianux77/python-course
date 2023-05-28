#creando funciones con lambdan
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5))

#creando funcion comun que diga si es par o no
numeros=[1,2,3,4,5,6,7,8,9,11,13,14,15,20]

def es_par(num):
    if(num% 2 == 0):
        return True

#usando filter con una funcion comun
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares)) 

#usando con lambda
numeros_pares_1 = filter(lambda numero: numero % 2 == 0, numeros)
print(list(numeros_pares_1)) 