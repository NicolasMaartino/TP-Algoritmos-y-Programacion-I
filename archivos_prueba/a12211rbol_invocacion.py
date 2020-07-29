#!/usr/bin/env python3
from reutilizacion import funciones_invocadas

def crear_arbol(invocaciones):
    print(invocaciones)
    arbol = ""
    for funcion,llamado in invocaciones.items():
        arbol = funcion + "--->"
        for claves_internas in llamado.keys():
            for i in invocaciones:
                if claves_internas in invocaciones:
                    if claves_internas  
            print(salida)        

fuente_unico=open("fuente_unico.csv","r")
invocaciones=funciones_invocadas(fuente_unico)
crear_arbol(invocaciones)
fuente_unico.close()