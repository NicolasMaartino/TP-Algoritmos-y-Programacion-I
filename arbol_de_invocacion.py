from reutilizacion import funciones_invocadas, crear_filas 
from generales import listar_archivo
from archivos import leer_linea_clasico

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
                    print("\t               ---> {}({})".format(value,dic_lineas[value]), end = "")
            print("\n")


