#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Diferencias de duracion

diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencia_con_max = 100 - (dalto_curso * 1000 //  otros_cursos_max / 10)
diferencia_con_promedio = 100 - (dalto_curso / otros_cursos_promedio * 100)



print(f'el curso de dalto dura {diferencia_con_min}% menos que el mas rapido')
print(f'el curso de dalto dura {diferencia_con_max}% menos que el mas lento')
print(f'el curso de dalto dura {diferencia_con_promedio}% menos que el promedio ')
print("----------------------------------")
# Duracion de crudos (videos sin editar)

crudo_promedio = 5
crudo_dalto = 3.5

# CALCULANDO EL PORCENTAJE DE TIEMPO VACIO REMOVIDO

tiempo_vacio_promedio = 100 - (otros_cursos_promedio * 1000 // crudo_promedio / 10)
tiempo_vacio_dalto = 100 - (dalto_curso * 1000 // crudo_dalto / 10)
# mostrando la cantidad de espacios vacios que se remueven (ejercicio B)

print(f'Un curso promedio elimina un {tiempo_vacio_promedio} % de tiempo vacio')
print(f'Este curso eliminó el {tiempo_vacio_dalto} % de tiempo vacio')
print("----------------------------------")
# mostrando diferencia si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')

print(f'Ver 10 horas de otro curso equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este cursos')
print("----------------------------------")