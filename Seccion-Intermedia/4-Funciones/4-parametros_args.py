#utilizando el parametro args
def sumas(*numeros):         # este args solo se usa al final del parametro.
    return sum(numeros)

resultado = sumas(5,3,9,10,20,3)
print(resultado)

#la misma forma con 2 parametros

def suma2(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado2 = suma2("Frank",5,3,10,10,5)
print(resultado2)

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado3 = suma_total([5,3,9,10,20,3])
print(resultado3)