#creando una funcion que nos devuelva losnumeros primos entre 0 y el argumento que pasamos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    for i in range(2,num-1):
        #si es divisble por alguno y es igual al cero, retornamos false y termina bucle
        if num % i == 0 : return False
        #si termina el bucle, significa que no fue divisible entonces es primo
    return True

#creando una funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        if resultado == True : primos.append(i)
    #devilvemos la lista
    return primos
#creamos el resultado llamando a la funcion y lo mostramos     
resultado = primos_hasta(30)
print(resultado)