numeros = [4,7,1]


#encontrando el numero mayor de una lista 
numero_mas_alto = max(numeros)

print(numero_mas_alto)

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)

print(numero_mas_bajo)

# redondeando a 6 decimales
numero = round(12.345678,2)           #round sirve para redondear decimales, y para decir cuando decimales figure
print(numero)

# retorna False -> 0,vacio,False,None / True -> distinto a 0, cadena de texto, datos no vacios

resultado_bool = bool([])   
print(resultado_bool)

#retorna True, si todos los valores son verdaderos 
resultado_all = all(["true",[344,23]])         # si hay un 0, False, None retorna -> False
print(resultado_all)


#suma  todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)