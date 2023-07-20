import re

texto ="""hola maestro como estas , esta es la cadena 1.  como esta mi capitan.
Estas es la segunda linea de texto. 
Y estas es la 3 linea""" 

#busca en una variable su calor que le indiquemos dentro de dicha variable
# resultado = re.search("hola",texto)

#busca todas las palabra "esta" dentro de la variable
# resultado1 = re.findall("esta",texto,flags=re.IGNORECASE)# flags=re.IGNORECASE : ignora las mayusculas y minusculas

#EXPRESIONES REGULARES
#\d - busca digitos digitos numericos 0-9
# resultado2 = re.findall(r"\d",texto)

#\D - busca TODOS MENOS digitos numericos 0-9
# resultado3 = re.findall(r"\D",texto)

#\w - busca caracteres alfanumerico [a-z A-Z 0-9 _ ] # W: mayuscula busca todos menos alfanumerico  
# resultado4 = re.findall(r"\w",texto)


#\s - busca espacio en blanco -> espacio, tabs, saltos de linea # S: mayuscula busca todos menos espacio en blaco  
# resultado5 = re.findall(r"\s",texto)


#\n -> los salto en linea #. -> busca lo inverso  
# resultado6 = re.findall(r"\n",texto)

#\ -> cancela caracteres especiales, cancelando la funcion del punto y buscando puntos
# resultado7 = re.findall(r"\.",texto)

#armando una cadena que busque numero, seguido de un punto y un espacio
# resultado8 = re.findall(f'\d\.\s',texto)

#^ -> busca el comienzo de una linea
# resultado9 = re.findall(f'^hola',texto,flags=re.M)

#$ -> busca el final de una linea
resultado0 = re.findall(f'linea$',texto)

#{n} -> busca n cantidad de veces el valor de la izquierda
#resultadoa = re.findall(f'\d{3}',texto) # 3 digitos juntos


#{n,m} -> al menos n, como maximo m.
#resultadob = re.findall(f'\d{1,4}',texto)

# | -> busca una cosa a la otra


#print(resultado)
#print(resultado1)
#print(resultado2)
#print(resultado3)
#print(resultado4)
#print(resultado5)
#print(resultado6)
#print(resultado7)
#print(resultado8)
#print(resultado9)
print(resultado0)