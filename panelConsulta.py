def formateo_linea(lista):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Funcion que hace que cada linea no tenga mas de 80 caracteres]"""
    n=0
    acumulador=0
    nueva_lista=lista.split()
    while len(nueva_lista)!=n:
        acumulador+=len(nueva_lista[n])
        n+=1
        if acumulador<=70 and acumulador>55:
            nueva_lista.insert(n, "\n")
            acumulador=0
    lista=" ".join(nueva_lista)
    return lista

def imprimir_todo(archivo, lista_funcion, lista_comentarios):
    """[Autor : Juan Godoy]"""
    """[Ayuda : imprime en un archivo .txt lo relacionado con la opcion ?]"""
    if len(lista_funcion[1])>80 or len(lista_comentarios[2]):
        lista_funcion[1]=formateo_linea(lista_funcion[1])
        lista_comentarios[2]=formateo_linea(lista_comentarios[2])
    archivo.write("-------------------------------------------------\n")
    archivo.write("Función: {0}\r\nAyuda: {1}\r\nParametros: {2}\r\nModulo: {3}\r\nAutor: {4}\n".format(lista_funcion[0], lista_comentarios[2], lista_funcion[1], lista_funcion[2], lista_comentarios[1]))
    archivo.write("-------------------------------------------------\n")
    
def opcion_todo (nombre, archivo_funciones, archivo_comentarios):
    """[Autor: Juan Godoy]"""
    """[Ayuda : Funcion que imprime todo lo relacionado con las funciones ?todo, #todo, e imprimir ?todo]"""
    from modulo_generico import leer_archivo
    from modulo_diseños import formato_interrogacion, formato_numeral
    ayuda_funciones=open("ayuda_funciones.txt", "w") 
    contador=0
    archivo_funciones.seek(0)
    archivo_comentarios.seek(0)
    
    linea=leer_archivo(archivo_funciones)
    
    while linea!=[""]:
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
        linea=leer_archivo(archivo_funciones)
    ayuda_funciones.close()
    return 
    

def buscar_funciones(archivo, funcion):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Va buscando en los archivos la funcion que necesito]"""
    from modulo_generico import leer_archivo
    linea=leer_archivo(archivo)
    while funcion!= linea[0]:
        if linea !=[""]:
            linea=leer_archivo(archivo)
        else:
            funcion=""
    return linea



def opciones_funcion(valor, archivo_funciones, archivo_comentarios):
    """[Autor : Juan Godoy]"""
    """[ayuda : Segun la opcion que se elija, se imprime diferente informacion sobre las funciones]"""
    from modulo_diseños import formato_interrogacion, formato_numeral
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
        
        
def panel_consultas():
    """[Autor : Juan]"""
    """[Ayuda : Funcion principal que pide el ingreso de una funcion y segun la opcion que elijas, imprime diversas cosas]"""
    from tabla_1 import tabla_consultas
    fuente_unico=open("fuente_unico.csv", "r")
    comentarios=open("comentarios.csv", "r")
    tabla_consultas(comentarios)
    valor_solicitado=input("\n Función: ")
    while valor_solicitado:
        if valor_solicitado=="imprimir ?todo" or valor_solicitado=="?todo" or valor_solicitado=="#todo":
            opcion_todo(valor_solicitado, fuente_unico, comentarios)
        else:
            opciones_funcion(valor_solicitado,fuente_unico, comentarios)
        valor_solicitado=input("\n Función: ")
        
    fuente_unico.close()
    comentarios.close()

""""""
    

