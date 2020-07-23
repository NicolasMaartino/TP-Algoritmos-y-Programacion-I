from reutilizacion import funciones_invocadas, crear_filas 
from generales import listar_archivo


dic_prueba = {'analiza_codigo': {'generar_archivo': 2, 'leer_linea_string': 2, 'validar_linea': 1},
           'generar_archivo': {'grabar_archivo': 1},
           'grabar_archivo': {},
           'leer_linea': {"unir_linea" : 1},
           'leer_linea_string': {},
           'ordenamiento_insercion': {},
           'reemplazar_string': {},
           'seccion_comentarios': {'unir_linea': 3},
           'unir_linea': {},
           'validar_linea': {'leer_linea': 4, 'reemplazar_string': 3, 'seccion_comentarios': 1, 'unir_linea': 3}}


def busca_main(dic):
    """[Autor: Sofia y Lucia]"""
    """[Ayuda: Busca funciones que sea la función principal]"""
    main = ""   
    valores = list(dic.values())
    for key in dic.keys():
        contador = 0
        while (len(valores) > contador) and (key not in list(valores[contador].keys())):
            if (contador == len(valores) - 1):
                main = key
            contador += 1

    return main

def cant_lineas(lista_ar_fu, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de lineas por funcion]"""
    
    for funcion in lista_ar_fu:
        dic[funcion[0]]["lineas"] = len(funcion) - 2
        
    return dic

def esquema(dic, main):
    
    for key in dic[main].keys():
        if key != "lineas":
            print("{}({}) --> {}({})".format(main, dic[main]["lineas"], key, dic[key]["lineas"]))
            for n in range(0, dic[main][key]-1):
                if ((list(dic[key].keys()))[0] != "lineas"):
                    print("                       {}({}) --> {}({})".format(key, dic[key]["lineas"], list(dic[key].keys())[0]), )
                else:
                    print("                       {}({})".format(key, dic[key]["lineas"]))


def esquema_arbol(dic, main):
    
    for key, invocacion in dic.items():
        print("{}({})".format(key, invocacion["lineas"]), end="")
        for i in invocacion.items():
            if i[0] != "lineas":
                string = "--->" + i[0]
                print("{:>25}({})".format(string, i[1]))
        print("\n")
    
  
    
    
fuente_unico = open("fuente_unico.csv", "r") # Borrar y pasar como parametro
lista_ar = listar_archivo(fuente_unico)
fuente_unico.close()
fuente_unico = open("fuente_unico.csv", "r")
diccionario = funciones_invocadas(fuente_unico)
dic2 = cant_lineas(lista_ar, diccionario)
busca_main(dic2)


fuente_unico.close()
""""""