#!/usr/bin/env python3
from tabla2 import imprimir

def leer_archivos_csv (archivocsv):
    """ Autor : Alejandro """
    """ Ayuda : leer archivos .csv y devuelve una lista de cada linea del archivo """
    linea = archivocsv.readline()
    return linea.rstrip('\n').split(',') if linea else ""
    
def informacion_desarrolladores():
    """Autor : Alejandro"""
    """Ayuda : Trae de Comentarios.csv y Fuente_Unico.csv nombre de funciones,autor, cantidad de lineas
                y cantidad de funciones. Luego del mismo modo que se muestra en pantalla es puesto en un
                archivo de texto plano""" 
    total_lineas = 0
    dicc_desarrolladores = {}
    with open("comentarios.csv","r") as comentarios,\
        open("fuente_unico.csv","r") as fuente_unico:
            linea_comentarios = leer_archivos_csv(comentarios)
            linea_fuente_unico = leer_archivos_csv(fuente_unico)
            while linea_comentarios and linea_fuente_unico:
                total_lineas += len(linea_fuente_unico[3:])
                if linea_comentarios[1].strip() in dicc_desarrolladores:
                    dicc_desarrolladores[linea_comentarios[1].strip()].append([linea_fuente_unico[0],len(linea_fuente_unico[3:])])
                else:
                    dicc_desarrolladores[linea_comentarios[1].strip()] = [[linea_fuente_unico[0],len(linea_fuente_unico[3:])]]
                linea_fuente_unico = leer_archivos_csv(fuente_unico)
                linea_comentarios = leer_archivos_csv(comentarios)
    imprimir(dicc_desarrolladores,total_lineas)

informacion_desarrolladores()