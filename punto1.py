#!/usr/bin/env python3
import os

def leer(archivo):
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = ""
    return devolver

def guarda_codigo():
    with open("programas.txt", 'r') as programa:
        linea = leer(programa)
        while linea:
            with open(linea[0],'r') as codigo:
                with open("fuente_unico.csv",'w') as fuente_unico:
                    linea_fuente = leer(codigo)
                    while linea_fuente:
                        fuente.write("".join(linea_fuente))
                        linea_fuente = leer(codigo)
            linea = leer(programa)
                    


guarda_codigo()



