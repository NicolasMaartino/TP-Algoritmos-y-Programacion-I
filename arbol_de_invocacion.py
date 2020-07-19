from reutilizacion_codigo import funciones_invocadas, crear_filas 
from generales import listar_archivo


dic_prueba = {'analiza_codigo': {'generar_archivo': 2, 'leer_linea_string': 2, 'validar_linea': 1},
           'generar_archivo': {'grabar_archivo': 1},
           'grabar_archivo': {},
           'leer_linea': {},
           'leer_linea_string': {},
           'ordenamiento_insercion': {},
           'reemplazar_string': {},
           'seccion_comentarios': {'unir_linea': 3},
           'unir_linea': {},
           'validar_linea': {'leer_linea': 4, 'reemplazar_string': 3, 'seccion_comentarios': 1, 'unir_linea': 3}}


def busca_main(fuente_unico):
    """[Autor: Sofia y Lucia]"""
    """[Ayuda: Busca funciones que sea la función principal]"""
    main = []
    fuente_unico = open("fuente_unico.csv", "r") # Borrar y pasar como parametro
    dic = funciones_invocadas(fuente_unico)
    valores = list(dic.values())
    for key in dic.keys():
        contador = 0
        while (len(valores) > contador) and (key not in list(valores[contador].keys())):
            if (key not in main) and (contador == len(valores) - 1):
                main.append(key)
            contador += 1

    return main
        
