
#Mas o menos esta es mi idea para la tabla, faltan detalles y mejorarla visualmente(cosas del format, tengo que alinearlos y demas).
#Si saben como hacer un codigo mas limpio, si hice algo mal o tienen alguna idea para mejorarlo, me dicen y lo hacemos en un toque.



def leer_archivo(archivo):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Funcion que lee lineas de un archivo]"""
    linea=archivo.readline()
    if linea:
        lista=linea.rstrip("\n").split(",")
    else:
        lista=[""]
    return lista


