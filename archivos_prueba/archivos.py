#!/usr/bin/env python3

def grabar_archivo (archivo,leyenda) :
    
    """[Autor : Nicolas]"""
    """[Ayuda : Graba linea en un archivo pasado por parametro] """
    
    archivo.write(leyenda)

def generar_archivo (lista,ruta) :
    """[Autor : Nicolas]"""
    """[Ayuda : Genera un archivo a traves de un iterable, y si lo necesitas te lo devuelve abierto]"""
    
    archivo = open(ruta,"w")
    for funcion in lista:
        leyenda = ",".join(funcion)+"\n"
        grabar_archivo(archivo,leyenda)

    archivo.close()

def leer_linea_string (archivo) :
    """[ Autor : Nicolas]"""
    """[Ayuda : lee una linea de un archivo y devuelve un string]"""
    
    return archivo.readline().strip()

def leer_linea (archivo) :
    
    """[Ayuda : lee una linea del archivo y devuelve una lista]"""
    
    # Esta a diferencia de la otra leer_linea ya corta por espacio con el split()
    
    linea = archivo.readline().strip().split()
    if linea:
        devolver = linea
    else:
        devolver = "","",""
    """[Autor : Nicolas]"""

    return devolver

""""""