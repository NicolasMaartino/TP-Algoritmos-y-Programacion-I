#!/usr/bin/env python3
from archivos import leer_linea_clasico


def funcion_principal():
    fin = False
    with open("fuente_unico.csv","r") as fuente:
        linea = leer_linea_clasico(fuente,",")
        while linea[0] and fin == False:
            main = linea[0] + '()'
            if main in linea[3:]:
                invocaciones_primarias = [funcion for funcion in linea[3:] if '()' in funcion]
                fin = True
            linea = leer_linea_clasico(fuente,",")
    print(invocaciones_primarias)
        


funcion_principal()


