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
        print(valores[contador])
        while (len(valores) > contador) and (key not in list(valores[contador].keys())):
            if (contador == len(valores) - 1):
                main = key
            contador += 1

    return main


def cant_lineas(lista_ar_fu):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de lineas por funcion]"""
    
    dic = {}
    for funcion in lista_ar_fu:
        dic[funcion[0]] = (len(funcion) - 2)
        
    return dic

def arbol(diccionario,dic_lineas):
    main = "analiza_codigo"
    print("{}({}) ".format(main,dic_lineas[main]),end = "")
    for key in diccionario[main].keys():
        if key != "":
            print("{}---> {}({}) ".format(" "*len(main) + "  ",key,dic_lineas[key]),end = "")
            for value in diccionario[key].keys():
                print("---> {}({})".format(value,dic_lineas[value]), end = "")
            print("\n")
                        
def imprimir(lista,dic_lineas):
    main = "analiza_codigo"
    fila_2 = ""
    if main in lista:
        fila_1 = ""
        fila_1 += "{}({})".format(main,dic_lineas[main])
        for c in lista:
            if c not in main:
                linea = dic_lineas[c]
                fila_2 += "{}({})".format(c,linea)
        print("{} ---> {}".format(fila_1, fila_2))
        
  
    
fuente_unico = open("fuente_unico.csv", "r") # Borrar y pasar como parametro
lista_ar = listar_archivo(fuente_unico)
fuente_unico.close()
fuente_unico = open("fuente_unico.csv", "r")
diccionario = funciones_invocadas(fuente_unico)
dic2 = cant_lineas(lista_ar)
dic=busca_main(dic2)
arbol(dic_prueba,dic2)

fuente_unico.close()
