#!/usr/bin/env python3
def leer_archivos_csv(archivocsv):
    """ Autor : Alejandro """
    """ Ayuda : leer archivos .csv y devuelve una lista de cada linea del archivo """
    linea = archivocsv.readline()
    return linea.rstrip('\n').split(',') if linea else ""