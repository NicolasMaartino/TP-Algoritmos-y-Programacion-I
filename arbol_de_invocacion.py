"""
Diagrama que gráfica la interacción entre las funciones, indicando quien llama a qué función.
El valor que se encuentra entre paréntesis es la cantidad de líneas que tiene la función.
"""

from reutilizacion_codigo import funciones_invocadas, crear_filas # La clave es la funcion que invoca y el valor es la funcion invocada
from generales import listar_archivo

dic = {'analiza_codigo': {'generar_archivo': 2, 'leer_linea_string': 2, 'validar_linea': 1},
       'generar_archivo': {'grabar_archivo': 1},
       'grabar_archivo': {},
       'leer_linea': {},
       'leer_linea_string': {},
       'ordenamiento_insercion': {},
       'reemplazar_string': {},
       'seccion_comentarios': {'unir_linea': 3},
       'unir_linea': {},
       'validar_linea': {'leer_linea': 4, 'reemplazar_string': 3, 'seccion_comentarios': 1, 'unir_linea': 3}}


def busca_main():
    main = []
    fuente_unico = open("fuente_unico.csv", "r")
    dic = funciones_invocadas(fuente_unico)
    valores = list(dic.values())
    
    for key in dic.keys():
        while key not in main:
            if key not in valores[0]:
                main.append(key)
                
    return main
        
busca_main()