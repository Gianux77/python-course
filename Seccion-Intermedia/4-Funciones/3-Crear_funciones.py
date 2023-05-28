#creando funciones simples


def saludar():
    print("Hola loco, como andas, tanto tiempo")
    
saludar()
saludar()
saludar()

#creando funciones con prarmetros

def saludar(nombre):
    print(f'Hola {nombre} como andas, que es de tu vida')
    
saludar("franco")

#creando funciones con 2 parametros

def saludar2(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif ( sexo == "hombre"):
        adjetivo = "maquina"
    else:
        adjetivo = "crack"
        
    print(f'hola {nombre}, mi {adjetivo}, ¿como andas? ')
    
saludar2("gian","hombre")

#creando una funcion que nos retorne valores
def contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña

password = contraseña_random(4)
print(password)