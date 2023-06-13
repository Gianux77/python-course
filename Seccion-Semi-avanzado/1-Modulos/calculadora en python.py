def Suma(num1, num2):
    return num1 + num2

def Resta(num3,num4):
    return  num3-num4

def Multiplicacion(num5,num6):
    return  num5 * num6

def Divison(num7,num8):
    return num7 / num8

opcion = int(input("ingrese que opcion quiere, solo hay 4, 1.suma 2.resta 3.multiplicacion 4.division: "))
dato1 = int(input("Ingrese su primer numero: "))
dato2 = int(input("Ingrese su segundo numero: "))

def Calculadora(dig1, dig2) :
    print(opcion)
    if opcion == 1:
        print(f'su resultado es: {Suma(dig1,dig2)}')
    elif opcion == 2 :
        print(f'su resultado es : {Resta(dig1,dig2)}')
    elif opcion == 3 :
        print(f'su resultado es : {Multiplicacion(dig1,dig2)}')
    elif opcion == 4 :
        print(f'su resultado es : {Divison(dig1,dig2)}')
    else:
        print("lo siento dato no invalido")

print(Calculadora(dato1,dato2))
