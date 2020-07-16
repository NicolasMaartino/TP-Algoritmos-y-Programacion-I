#Es la base del panel de consultas, me falta hacerlo ciclico, agregar excepciones, las funciones ?todos y #todos
#Tengo que hacerlo mas estetico (Mi punto debil en la vida y en python)
#Y crear el archivo ayuda_funciones.txt
#La mayoria de esto se hace entorno a este codigo, asique no hay drama.
#Si ven algo que esta mal, hay algo para mejorar o lo que les pinte, me avisan y lo hacemos en un toque.


def buscar_funciones(archivo, funcion):
    """[Autor : Juan]"""
    """[Ayuda : Va buscando en los archivos la funcion que necesito]"""
    from modulo_generico import leer_archivo
    linea=leer_archivo(archivo)
    while funcion!= linea[0]:
        linea=leer_archivo(archivo)
    return linea

def panel_consultas():
    """[Autor : Juan]"""
    """[Ayuda : Lo que hace esta funcion es pedir el ingreso de una funcion y segun la opcion que elijas, imprime diversas cosas]"""
    
    fuente_unico=open("fuente_unico.csv", "r")
    comentarios=open("comentarios.csv", "r")
    
    valor_solicitado=input("Función: ")
    nombre_funcion=valor_solicitado.replace(valor_solicitado[-1], "")
    
    
    lista_comentarios = buscar_funciones(comentarios, nombre_funcion)
    lista_funciones = buscar_funciones(fuente_unico, nombre_funcion)
    
    if valor_solicitado.endswith("?"):
        print("{0} {1} {2} {3} {4}".format(lista_funciones[0], lista_comentarios[2], lista_funciones[1], lista_funciones[2], lista_comentarios[1]))
        
    elif valor_solicitado.endswith("#"):
        print("{0}\r\n{1}".format(lista_funciones, lista_comentarios))

    fuente_unico.close()
    comentarios.close()
        
    return
        


panel_consultas()

