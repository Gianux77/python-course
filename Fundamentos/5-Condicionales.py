# si una condicion se cumple true si no se cumple false.

#if-else

edad = 17

if edad >= 18:
    print("podes pasar")

else:
    print("no podes pasar")

# otro ejemplo

contraseña_almacenada = "frankMaestro"
contraseña_escrita = 'frankMaestro'


if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SESION")

else:
    print("CONTRASEÑA INCORRECTA, INTENTE DE NUEVO")
    

# ELSE-IF

ingreso_mensual = 5000

if ingreso_mensual > 10000:
    print("esta bien en cualquier parte del mundo")

elif ingreso_mensual > 1000:
        print("esta bien en latinoamerica")
else:
    print("sos pobre")

