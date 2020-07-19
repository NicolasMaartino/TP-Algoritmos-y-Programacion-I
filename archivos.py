#!/usr/bin/env python3

def buscar_funciones (archivo, funcion):
    """[Autor : Juan]"""
    """[Ayuda : Va buscando en los archivos la funcion que necesito]"""
    linea=leer_archivo(archivo)
    while funcion!= linea[0]:
        if linea !=[""]:
            linea=leer_archivo(archivo)
        else:
            funcion=""
    return linea

def abrir_archivos (nombre_archivo,modo):
    """[Autor : Nicolas]"""
    """[Ayuda : Abre un archivo]"""
    archivo = open(nombre_archivo,modo)
    return archivo

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

def leer_linea (archivo,corte) :
    
    """[Ayuda : lee una linea del archivo y devuelve una lista]"""
    
    # Esta a diferencia de la otra leer_linea ya corta por espacio con el split()
    
    linea = archivo.readline().strip().split(corte)
    if linea[0]!="":
        devolver = linea
    else:
        devolver = "","",""
    """[Autor : Nicolas]"""

    return devolver

""""""
