with open("Seccion-Semi-avanzado\\2-Archivos\\texto_de_frank.txt","w") as archivo:
    # soobrescribiendo el archivo
    # archivo.write("argentina campeona del mundo de 2022")
    
    #writelines: sobreescribiendo lineas
    #agregando 2 lineas
    archivo.writelines(["Hola maestro como andas\n","vamos a jugar pa"])
    
    #agregando mas 2 lineas mas
    archivo.writelines(["\nte prendes para un asado","\nque decis"])