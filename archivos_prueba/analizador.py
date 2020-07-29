#!/usr/bin/env python3
from leer_archivos import leer_archivos_csv

def veces_invocaciones():
    """
    Autor : Sofia Marchesini
    Ayuda : esta funcion crea un dicionario compuesto por
    la clave como la funcion invocada y el valor
    como las veces que esta funcion fue invocada
    """
    cont = 0
    invocaciones = {}
    dicc = {}
    with open("fuente_unico.csv") as fuente:
        linea_archivo = leer_archivos_csv(fuente)
        linea_archivo_d = leer_archivos_csv(fuente)
        while linea_archivo:
            while linea_archivo_d:
                invocaciones[linea_archivo[0]] = {}
            linea_archivo = leer_archivos_csv(fuente)

    print(invocaciones)

veces_invocaciones()