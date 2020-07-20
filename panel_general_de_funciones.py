
#!/usr/bin/env python3
"""
Panel general de Funciones
Mediante esta opción se debe mostrar por pantalla, una tabla con la siguiente información
por columna.
"""
import tabla
from generales import listar_archivo
from archivos import grabar_archivo
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
        funciones[funcion[0]]["return"] = 0
        funciones[funcion[0]]["if"] = 0
        funciones[funcion[0]]["elif"] = 0
        funciones[funcion[0]]["for"] = 0
        funciones[funcion[0]]["while"] = 0
        funciones[funcion[0]]["break"] = 0
        funciones[funcion[0]]["exit"] = 0
        funciones[funcion[0]]["Coment"] = 0
        funciones[funcion[0]]["Ayuda"] = ""
        funciones[funcion[0]]["Autor"] = ""
    return funciones

def contador (elementos, lista_ar, dic):
    """[Autor: Lucia]
        [Ayuda: Cuenta la cantidad de veces que aparece el elemento que se le le pasa por parametro]"""
    for elemento in elementos:
        for funcion in lista_ar:
            for i in range(3, len(funcion)): 
                dic[funcion[0]][elemento] += funcion[i].count(elemento)

    return dic


def invocaciones(lista_ar, dic):
    """[Autor: Lucia]
       [Ayuda: Cuenta la cantidad de veces que fue invocada cada funcion]"""

    for key in dic:
        for funcion in lista_ar: 
            for i in range(2, len(funcion)):
                dic[key]["Invocaciones"] += funcion[i].count(key)

    return dic

def lineas_coment(lista_ar, dic):
    """[Autor: Lucia]
       [Ayuda: cuenta las lineas de comentarios que no sean de autor o ayuda]"""
    for funcion in lista_ar:
        if (len(funcion) > 3):
            dic[funcion[0]]["Coment"] += len(funcion) -3
    return dic

def ayuda(lista_ar, dic):
    """[Autor: Lucia]
       [Ayuda: verifica si hay o no un comentario de ayuda dentro de la función]"""
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
    contador(["for","while","break","exit","return","if","elif"], lista_fu, dic)
    lineas_coment(lista_com, dic)
    ayuda(lista_com, dic)
    autor(lista_com, dic)
    return dic

def grabar_linea(valor,nombre,if_elif,archivo,valor_final):
    
    if nombre == "if" or nombre == "elif":
        valor_final += valor
        if_elif.remove(nombre)
        if len(if_elif)==0:
            leyenda = str(valor_final) + ","
            grabar_archivo(archivo,leyenda)
    elif nombre == "Parametros":
        if len(valor) == 0:
            valor = 0
            leyenda = str(valor) + ","
            grabar_archivo(archivo,leyenda)
        else:
            parametros = valor.count(" ")+1
            leyenda = str(parametros) + ","
            grabar_archivo(archivo,leyenda)
    else:
            
        leyenda = str(valor) + ","
        grabar_archivo(archivo,leyenda)
    return if_elif


def generar_archivo(dic):
    
    archivo = open("panel_general.csv","w")
    lista = ["Funcion,","Parametros,","lineas,","invocaciones,","Returns,","If/Elif,","For,","While,","Break,","Exit,","Coment,","Ayuda,","Autor"]
    for elemento in lista:
        archivo.write(elemento)
    archivo.write("\n")
    for funcion_principal in dic:
        if_elif = ["if","elif"]
        valor_final = 0
        for valores in dic[funcion_principal]:
            valor = dic[funcion_principal][valores]
            # Esta funcion ejecutara todo el proceso para meter la linea en el archivo
            if_elif = grabar_linea(valor,valores,if_elif,archivo,valor_final)
        archivo.write("\n")
    archivo.close()




def panel_general(fuente_unico,comentarios):
    """[Autor: Lucia]"""
    """[Ayuda: ejecuta todo, es el main del programa]"""

    lista_fuente_unico = listar_archivo(fuente_unico) # Cambiarle el parametro de listar_archivo
    lista_comentarios = listar_archivo(comentarios) # importar el archivo
    diccionario = org_archivo(lista_fuente_unico)
    dic_final = unir(diccionario, lista_fuente_unico, lista_comentarios)
    generar_archivo(dic_final)
    tabla.imprimir_panel(dic_final)


""""""
    
