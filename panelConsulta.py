
def opcion_todo (nombre, archivo_funciones, archivo_comentarios):
    """[Autor: Juan Godoy]"""
    """[Ayuda : Funcion que imprime todo lo relacionado con las funciones ?todo, #todo, e imprimir ?todo]"""
    from archivos import leer_linea, buscar_funciones
    from tabla import formato_interrogacion, formato_numeral, imprimir_todo
    ayuda_funciones=open("ayuda_funciones.txt", "w") 
    contador=0
    archivo_funciones.seek(0)
    archivo_comentarios.seek(0)
    
    linea=leer_linea(archivo_funciones, ",")
    
    while linea[0]!="":
        nombre_funcion=linea[0]
        archivo_funciones.seek(contador)
        archivo_comentarios.seek(contador)
        
        lista_comentarios = buscar_funciones(archivo_comentarios, nombre_funcion)
        lista_funciones = buscar_funciones(archivo_funciones, nombre_funcion)
        contador+=1
        if nombre == "?todo":
            formato_interrogacion(lista_funciones, lista_comentarios)
        elif nombre=="imprimir ?todo":
            imprimir_todo(ayuda_funciones, lista_funciones, lista_comentarios)
        else:
            formato_numeral(lista_funciones, lista_comentarios)
        linea=leer_linea(archivo_funciones, ",")
    ayuda_funciones.close()
    return 
    

def opciones_funcion(valor, archivo_funciones, archivo_comentarios):
    """[Autor : Juan Godoy]"""
    """[ayuda : Segun la opcion que se elija, se imprime diferente informacion sobre las funciones]"""
    from tabla import formato_interrogacion, formato_numeral
    from archivos import buscar_funciones
    if valor == "?todo" or valor == "#todo" or valor =="imprimir ?todo":
        opcion_todo (valor, archivo_funciones, archivo_comentarios)
    else:
        nombre_funcion=valor.replace(valor[-1], "")
        
        archivo_comentarios.seek(0)
        archivo_funciones.seek(0)
        
        lista_comentarios = buscar_funciones(archivo_comentarios, nombre_funcion)
        lista_funciones = buscar_funciones(archivo_funciones, nombre_funcion)
        
        if (valor.endswith("?")) and (lista_comentarios!=[""]) and (lista_funciones!=[""]):
            formato_interrogacion(lista_funciones, lista_comentarios)
        elif (valor.endswith("#")) and (lista_comentarios!=[""]) and (lista_funciones!=[""]):
            formato_numeral(lista_funciones, lista_comentarios)
        else:
            print("\nPorfavor ingrese un nombre de funcion valido seguido de ? o #. \n")
    return 
        
        
def panel_consultas(fuente_unico, comentarios):
    """[Autor : Juan]"""
    """[Ayuda : Funcion principal que pide el ingreso de una funcion y segun la opcion que elijas, imprime diversas cosas]"""
    from tabla import tabla_consultas
    tabla_consultas(comentarios)
    valor_solicitado=input("\nFunción: ")
    while valor_solicitado:
        if valor_solicitado=="imprimir ?todo" or valor_solicitado=="?todo" or valor_solicitado=="#todo":
            opcion_todo(valor_solicitado, fuente_unico, comentarios)
        else:
            opciones_funcion(valor_solicitado,fuente_unico, comentarios)
        valor_solicitado=input("\nFunción: ")
        

    

    

