#!/usr/bin/env python3
from archivos import leer_linea_string

def invocacion_funciones():
    with open("fuente_unico.csv","r") as fuente:
        linea = (leer_linea_string(fuente)).rstrip('\n').split(',')
        while linea[0]:
            print(linea[0])
            if linea[0] in linea[3:]:
                print("hola")
            linea = (leer_linea_string(fuente)).rstrip('\n').split(',')
                
invocacion_funciones()