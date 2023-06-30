# 2 lista, una con nombres otra con apellidos
nombres = ["Tony","Bruce","Steve","Thor","Natasha","Clint"]
apellidos = ["Stark","Banner","Rogers","Odin","Romanoff","Barton"]

#Registrar esta informacion en un TXT de forma optima

with open("Seccion-Semi-avanzado\\3-Trabajando_con_Archivos\\nombre_apellidos.txt","w") as arch:
    arch.writelines("los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellidos: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]
    