cadena1 = "Hola Soy Dalto"
cadena2 = "Bienvenido maquinola"
cadena3 = "33" 
cadena4 = "starwars"
cadena5 = "Hola,soy,chatGPT,como,estas"


resultado = dir(cadena1)

print(resultado)

# funcionamiento: DATO.metodo()

# ** METODOS QUE CONVIERTE **
# convierte la cadena en mayuscula
resultado1 = cadena1.upper()  
print(resultado1)

# convierte la cadena en minuscula
resultado2 = cadena1.lower() 
print(resultado2)

# convierte la primera letra en mayuscula
resultado3 = cadena1.capitalize() 
print(resultado3)

# ** METODOS QUE BUSCAN **
# buscamos una cadena en otra cadena, si no la encuentra retorna -1
resultado4 = cadena1.find("a")  # posicion de la letra 
print(resultado4) # otra metodo a excepcion es el index


# ** METODOS QUE CONSULTA **
# si es numerico, devolvemos true, si no es devolvemos false

es_numerico = cadena3.isnumeric()
print(es_numerico)

# si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena4.isalpha()
print(es_alfanumerico)

# ** METODOS QUE BUSCAN_2 **
# contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")
print(contar_coincidencias)

# contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1) #(len es una funcion no es un metodo)
print(contar_caracteres)

# verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("Ho")
print(empieza_con)

# verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("Ho")
print(termina_con) 

# ** METODOS QUE REEMPLAZAN **
#reemplaza un pedazo de la cadena dada, por otra dada.
cadena_nueva = cadena1.replace("Dalto","Franco")
print(cadena_nueva)

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena5.split(",")
print(cadena_separada) # devuelve siempre un lista
