#Es la base del panel de consultas me falta la funcion #todo
#Tengo que hacerlo mas estetico (Mi punto debil en la vida y en python)
#Y crear el archivo ayuda_funciones.txt
#La mayoria de esto se hace entorno a este codigo, asique no hay drama.
#Si ven algo que esta mal, hay algo para mejorar o lo que les pinte, me avisan y lo hacemos en un toque.
#Hoy estoy bastante mal dormido asique nose que hice pero parece codigo.




def todo_interrogacion (archivo_funciones, archivo_comentarios):
    """[Autor: Juan]"""
    """[Ayuda : Funcion que imprime todo lo relacionado a el signo ? para todas las funciones]"""
    from modulo_generico import leer_archivo
    
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
        
        print("{0} {1} {2} {3} {4}".format(lista_funciones[0], lista_comentarios[2], lista_funciones[1], lista_funciones[2], lista_comentarios[1]))
        linea=leer_archivo(archivo_funciones)
    return
    
        

def buscar_funciones(archivo, funcion):
    """[Autor : Juan]"""
    """[Ayuda : Va buscando en los archivos la funcion que necesito]"""
    from modulo_generico import leer_archivo
    linea=leer_archivo(archivo)
    while funcion!= linea[0]:
        if linea !=[""]:
            linea=leer_archivo(archivo)
        else:
            funcion=""
    return linea



def panel_consultas():
    """[Autor : Juan]"""
    """[Ayuda : Funcion principal que pide el ingreso de una funcion y segun la opcion que elijas, imprime diversas cosas]"""
    fuente_unico=open("fuente_unico.csv", "r")
    comentarios=open("comentarios.csv", "r")
    valor_solicitado=input("Función: ")

    while valor_solicitado:
        if valor_solicitado == "?todo":
            todo_interrogacion (fuente_unico, comentarios)
        else:
            nombre_funcion=valor_solicitado.replace(valor_solicitado[-1], "")
        
            comentarios.seek(0)
            fuente_unico.seek(0)
        
            lista_comentarios = buscar_funciones(comentarios, nombre_funcion)
            lista_funciones = buscar_funciones(fuente_unico, nombre_funcion)
        
            if (valor_solicitado.endswith("?")) and (lista_comentarios!=[""]) and (lista_funciones!=[""]):
                print("{0} {1} {2} {3} {4}".format(lista_funciones[0], lista_comentarios[2], lista_funciones[1], lista_funciones[2], lista_comentarios[1]))
            elif (valor_solicitado.endswith("#")) and (lista_comentarios!=[""]) and (lista_funciones!=[""]):
                print("{0}\r\n{1}".format(lista_funciones, lista_comentarios))
            else:
                print("\nPorfavor ingrese un nombre de funcion valido seguido de ? o #. \n")
            
        valor_solicitado=input("Función: ")
        
    fuente_unico.close()
    comentarios.close()
        
    return
        


panel_consultas()



