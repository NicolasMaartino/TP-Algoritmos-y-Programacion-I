#!/usr/bin/env python3
"""
Panel general de Funciones
Mediante esta opción se debe mostrar por pantalla, una tabla con la siguiente información
por columna.
"""
import tabla

def leer_archivo(archivo):
    """[Autor: Lucia]"""
    """[Ayuda: Esta funcion lee el archivo y borra el salto de linea]"""
    linea = archivo.readline()
    if linea:
        linea = linea.strip("\n")
    else:
        linea = " , , , "
    return linea.split(",")

def listar_archivo(archivo):
    """[Autor: Lucia]"""
    """[Ayuda: convierte al archivo en una lista donde cada elemento es una linea del mismo]"""
    lista_ar = []
    linea = leer_archivo(archivo)
    while (linea[0] != ' '):
        lista_ar.append(linea)
        linea = leer_archivo(archivo)
    return lista_ar

def organizar_archivo(lista_ar):
    """[Autor: Lucia]"""
    """[Ayuda: Crea un diccionario donde la calve es el nombre de la funcion que a su vez tiene un diccionario adentro
        donde las claves son los atributos de las columnas]"""
    funciones = {}
    for funcion in lista_ar:
        funciones[funcion[0]] = {}
        funciones[funcion[0]]["Nombre"] = "{}.{}".format(funcion[0], funcion[2])
        funciones[funcion[0]]["Parametros"] = funcion[1].strip('()')
        funciones[funcion[0]]["Lineas"] = len(funcion) - 2 #Por los parametros y el modulo
        funciones[funcion[0]]["Invocaciones"] = 0
        funciones[funcion[0]]["Returns"] = 0
        funciones[funcion[0]]["If/elif"] = 0
        funciones[funcion[0]]["for"] = 0
        funciones[funcion[0]]["while"] = 0
        funciones[funcion[0]]["Break"] = 0
        funciones[funcion[0]]["Exit"] = 0
        funciones[funcion[0]]["Coment"] = 0
        funciones[funcion[0]]["Ayuda"] = ""
        funciones[funcion[0]]["Autor"] = ""
    return funciones

def invocaciones(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de veces que fue invocada cada funcion]"""

    for key in dic:
        for funcion in lista_ar: 
            for i in range(2, len(funcion)):
                dic[key]["Invocaciones"] += funcion[i].count(key)

    return dic

def returns(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de veces que aparece un return]"""
    
    for funcion in lista_ar:
        for i in range(3, len(funcion)):
            dic[funcion[0]]["Returns"] += funcion[i].count("return")

    return dic

def if_elif(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de veces que aparece un if o un elif]"""

    for funcion in lista_ar:
        for i in range(3, len(funcion)):
            dic[funcion[0]]["If/elif"] += funcion[i].count("if") + funcion[i].count("elif")
    return dic

def fors(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de fors que hay en una funcion]"""
    
    for funcion in lista_ar:
        for i in range(3, len(funcion)):
            dic[funcion[0]]["for"] += funcion[i].count("for")
    return dic
            
def whiles(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de whiles que hay en cada función]"""
    
    for funcion in lista_ar:
        for i in range(3, len(funcion)):
            dic[funcion[0]]["while"] += funcion[i].count("while")
    return dic

def breaks(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de breaks que hay en cada función]"""
    
    for funcion in lista_ar:
        for i in range(3, len(funcion)):
            dic[funcion[0]]["Break"] += funcion[i].count("break")
    return dic

def exits(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de exits que hay en cada función]"""
    
    for funcion in lista_ar:
        for i in range(3, len(funcion)):
            dic[funcion[0]]["Exit"] += funcion[i].count("exit")
    return dic

def lineas_coment(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: cuenta las lineas de comentarios que no sean de autor o ayuda]"""
    for funcion in lista_ar:
        if (len(funcion) > 3):
            dic[funcion[0]]["Coment"] += len(funcion) -3
    return dic

def ayuda(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: verifica si hay o no un comentario de ayuda dentro de la función]"""
    for funcion in lista_ar:
        if (funcion[2] == ''):
            dic[funcion[0]]["Ayuda"] = "No"
        else:
            dic[funcion[0]]["Ayuda"] = "Si"
    return dic

def autor(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Indica el nombre del autor de la función]"""
    for funcion in lista_ar:
        dic[funcion[0]]["Autor"] = funcion[1]
    return dic

def unir(dic, lista_fu, lista_com):
    """[Autor: Lucia]"""
    """[Ayuda: Une todas las funciones contadoras con el diccionario]"""
    invocaciones(lista_fu, dic)
    returns(lista_fu, dic)
    if_elif(lista_fu, dic)
    fors(lista_fu, dic)
    whiles(lista_fu, dic)
    breaks(lista_fu,dic)
    exits(lista_fu, dic)
    lineas_coment(lista_com, dic)
    ayuda(lista_com, dic)
    autor(lista_com, dic)
    return dic



ar_fuente = open('fuente_unico.csv', 'r')
ar_coment = open('comentarios.csv', 'r')
lista_fuente = listar_archivo(ar_fuente)
lista_coment = listar_archivo(ar_coment)
diccionario_ar = organizar_archivo(lista_fuente)
print(diccionario_ar)
tabla.imprimir(unir(diccionario_ar, lista_fuente, lista_coment))
ar_fuente.close()
ar_coment.close()