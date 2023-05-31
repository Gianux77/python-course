#creando una funcion que nos devuelva losnumeros primos entre 0 y el argumento que pasamos

def es_primo(num):
    for i in range(2,num-1):
        if num % i == 0 : return False
    return True

resultado = es_primo(13)
print(resultado)