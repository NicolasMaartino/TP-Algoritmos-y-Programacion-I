"""
Panel general de Funciones
Mediante esta opción se debe mostrar por pantalla, una tabla con la siguiente información
por columna.
"""

def leer_archivo(archivo):
    """
    [Autor: Lucia]
    [Ayuda: Esta funcion lee el archivo y borra el salto de linea]
    """
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
        funciones[funcion[0]]["Parametros"] = funcion[1]
        funciones[funcion[0]]["Lineas"] = len(funcion) - 2 #Por los parametros y el modulo
        funciones[funcion[0]]["Invocaciones"] = 0
        funciones[funcion[0]]["Returns"] = 0
        funciones[funcion[0]]["If/elif"] = 0
        funciones[funcion[0]]["for"] = 0
        funciones[funcion[0]]["while"] = 0
        funciones[funcion[0]]["Break"] = 0
        funciones[funcion[0]]["Exit"] = 0
        funciones[funcion[0]]["Coment"] = 0
        funciones[funcion[0]]["Ayuda"] = True
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
    

ar_fuente = open('fuente_unico1.csv', 'r')

lista_fu = listar_archivo(ar_fuente)
lista_com = listar_archivo(ar_coment)
diccionario_ar = organizar_archivo(lista_fu)
print(exits(lista_fu, diccionario_ar))
ar_fuente.close()