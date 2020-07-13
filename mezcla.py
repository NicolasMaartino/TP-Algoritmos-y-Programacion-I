#!/usr/bin/env python3
import csv
from os import remove
def leer_archivos_csv (archivocsv):
    """Autor : Alejandro"""
    """Ayuda : leer archivos .csv y devuelve una lista de ellos para un mejor estudio"""
    linea = archivocsv.readline()
    return linea.rstrip('\n').split(',') if linea else ""
def tipo_archivos (archivo):
    """Autor : Alejandro"""
    """Ayuda : valida si el archivo recibido es comentarios o fuente_unico"""
    if "comentarios" in archivo:
        archivo_unico = "comentarios_unificado.csv"
    else:
        archivo_unico = "fuente_unificado.csv"
    return archivo_unico
def guarda_archivo (archivo_aux,lista_archivos):
    """Autor: Alejandro"""
    """Lee el archivo auxiliar y vuelve a generar otro, eliminando luego el anterior"""
    archivo_mezcla = tipo_archivos(lista_archivos[0])
    with open(archivo_mezcla,"w") as prestaciones:
        with open(archivo_aux,"r") as auxiliar:
            entrada = csv.reader(auxiliar)
            ordenado = sorted(entrada, key=lambda fila: fila[0])
            for fila in ordenado:
                salida = csv.writer(prestaciones)
                salida.writerow(fila)
    remove(archivo_aux)
def merge (lista_archivos):
    """Autor : Alejandro"""
    """Mezcla Archivos CSV's"""
    archivo_aux="archivo_aux.csv"
    with open(archivo_aux,"w") as unificado:
        for archivo in lista_archivos:
            with open(archivo,'r') as arch:
                linea = leer_archivos_csv(arch)
                while linea:
                    entrada = csv.writer(unificado)
                    entrada.writerow(linea)
                    linea = leer_archivos_csv(arch)
    guarda_archivo(archivo_aux,lista_archivos)
