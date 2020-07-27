from reutilizacion import funciones_invocadas, crear_filas 
from generales import listar_archivo
from archivos import leer_linea_clasico

dic_prueba = {'acomodar_lectura': {'reemplazar_string': 1},
              'analisis_linea': {'acomodar_lectura': 4, 'comentarios': 1, 'indice_vaciado': 1},
              'analizador_funcion': {'acomodar_lectura': 7, 'analisis_linea': 1, 'buscar_dato': 1, 'encontrar_palabras': 1},
              'archivos': {'archivos': 3, 'eliminar_archivos': 1, 'proceso_archivos': 1, 'separador_archivos': 1},
              'autor': {}, 'ayuda': {}, 'borrador': {}, 'busca_principal': {}, 'buscar_dato': {}, 'cant_lineas': {},
              'carga_informacion_desarrollador': {'imprimir_tabla_desarrollador': 1}, 'comentarios': {'acomodar_lectura': 3},
              'contador': {}, 'crear_filas': {}, 'crear_tabla': {'crear_filas': 1, 'lista_de_funciones': 1},
              'eliminar_archivos': {}, 'encontrar_palabras': {}, 'extraigo_linea': {}, 'formato_interrogacion': {},
              'formato_numeral': {}, 'funciones_invocadas': {'veces_invocadas': 1},
              'guardar_archivo': {'archivos': 1, 'tipo_archivos': 1},
              'imprimir_analizador': {'crear_tabla': 1, 'funciones_invocadas': 1, 'lista_de_funciones': 1},
              'imprimir_diagrama': {'busca_principal': 1, 'cant_lineas': 1, 'funciones_invocadas': 1, 'listar_archivo': 1}, 'imprimir_panel': {},
              'imprimir_tabla_desarrollador': {}, 'imprimir_todo': {}, 'indice_vaciado': {},
              'info_desarrolladores': {'carga_informacion_desarrollador': 1, 'leer_archivos_csv': 4},
              'invocaciones': {'acomodar_lectura': 1, 'extraigo_linea': 1}, 'leer_archivos_csv': {}, 'lineas_coment': {}, 'lista_de_funciones': {}, 'listar_archivo': {},
              'main': {'menu': 1},
              'menu': {'archivos': 1, 'borrador': 2, 'imprimir_analizador': 1, 'imprimir_diagrama': 1, 'info_desarrolladores': 1, 'menu': 2, 'panel_consultas': 1, 'panel_general': 1, 'texto_menu': 2, 'validar_programa': 1}, 'mezcla': {'guardar_archivo': 1}, 'opcion_todo': {'formato_interrogacion': 1, 'formato_numeral': 1, 'imprimir_todo': 1}, 'opciones_funcion': {'formato_interrogacion': 1, 'formato_numeral': 1, 'reemplazar_string': 1}, 'ordenamiento_insercion': {}, 'organizar_archivo': {}, 'panel_consultas': {'opcion_todo': 1, 'opciones_funcion': 1, 'tabla_consultas': 1}, 'panel_csv': {'procesa_linea': 1}, 'panel_general': {'imprimir_panel': 1, 'listar_archivo': 2, 'organizar_archivo': 1, 'panel_csv': 1, 'unir': 1}, 'parametros': {}, 'procesa_linea': {}, 'proceso_archivos': {'acomodar_lectura': 2, 'analizador_funcion': 1, 'ordenamiento_insercion': 1, 'parametros': 1, 'reemplazar_string': 1, 'reunir_parametros': 1}, 'reemplazar_string': {}, 'reunir_parametros': {'acomodar_lectura': 1}, 'separador_archivos': {'mezcla': 2}, 'tabla_consultas': {}, 'texto_menu': {}, 'tipo_archivos': {}, 'unir': {'autor': 1, 'ayuda': 1, 'contador': 1, 'invocaciones': 1, 'lineas_coment': 1, 'parametros': 1}, 'validar_programa': {}, 'veces_invocadas': {'lista_de_funciones': 1}}

def busca_principal(dic):
    """[Autor: Sofia y Lucia]"""
    """[Ayuda: Busca la función principal de un programa]"""
    principal = ""   
    valores = list(dic.values())
    for key in dic.keys():
        contador = 0
        posible_principal = ""
        while (len(valores) > contador) and (key not in list(valores[contador].keys())):
            posible_principal = key
            if (contador == len(valores) - 1):
                principal = posible_principal
            contador += 1   
    return principal


def cant_lineas(lista_ar_fu):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de lineas por funcion]"""
    
    dic = {}
    for funcion in lista_ar_fu:
        dic[funcion[0]] = (len(funcion) - 2)
        
    return dic

def imprimir_diagrama(): 
    """[Autor : Sofia Marchesini]"""
    """[Ayuda : este codigo permite imprimir las funciones main
        con sus respectivas funciones invocadas y las funciones que a su vez
        estas invocan y asi sucesivamente]"""
        
    fuente_unico = open("fuente_unico.csv","r")
    lista_ar = listar_archivo(fuente_unico)
    fuente_unico.seek(0)
    diccionario = funciones_invocadas(fuente_unico)
    dic_lineas = cant_lineas(lista_ar)
    principal = busca_principal(diccionario)
    fuente_unico.close()
    print("{}({}) ".format(principal,dic_lineas[principal]),end = "")
    for key in diccionario[principal].keys():
        if key:
            print("---> {}({}) ".format(key,dic_lineas[key]),end="")
            for value in diccionario[key].keys():
                if value != key:
                    print("")
                    print("\t---> {}({})".format(value,dic_lineas[value]), end = "")
            print("\n")


