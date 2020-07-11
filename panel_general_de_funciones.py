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

def organizar_archivo(ar_fuente):
    """[Autor: Lucia]"""
    """[Ayuda: Crea un diccionario donde la calve es el nombre de la funcion que a su vez tiene un diccionario adentro
        donde las claves son los atributos de las columnas]"""
    ar_fuente = open('fuente_unico1.csv', 'r')
    funciones = {}
    funcion_fu = leer_archivo(ar_fuente) #fu: fuente unico
    while (funcion_fu[0] != ' '):
        funciones[funcion_fu[0]] = {}
        funciones[funcion_fu[0]]["Parametros"] = funcion_fu[1].strip("()")
        funciones[funcion_fu[0]]["Modulo"] = funcion_fu[2]
        funciones[funcion_fu[0]]["Lineas"] = len(funcion_fu) - 2
        funciones[funcion_fu[0]]["Invocaciones"] = 0
        funcion_fu = leer_archivo(ar_fuente)
    ar_fuente.close()
    return funciones

def invocaciones(ar_fuente, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de veces que fue invocada cada funcion]"""
    ar_fuente = open('fuente_unico1.csv', 'r')
    funcion_fu = leer_archivo(ar_fuente)
    while (funcion_fu[0] != ' '):
        for key in dic:
            for i in range(0, len(funcion_fu)):
                if key in funcion_fu[i]:
                    dic[key]["Invocaciones"] +=1
        funcion_fu = leer_archivo(ar_fuente)
    ar_fuente.close()
    return dic

def returns(ar_fuente, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de veces que aparece un return]"""
    ar_fuente = open('fuente_unico1.csv', 'r')
    funcion_fu = leer_archivo(ar_fuente)
    while (funcion_fu[0] != ' '):
        for key in dic:
            for i in range(0, len(funcion_fu)):
                dic[key]["Returns"] = funcion_fu[i].count("return")
        funcion_fu = leer_archivo(ar_fuente)
    ar_fuente.close()
    return dic

def if_elif(ar_fuente, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de veces que aparece un if o un elif]"""
    ar_fuente = open('fuente_unico1.csv', 'r')
    funcion_fu = leer_archivo(ar_fuente)
    while (funcion_fu[0] != ' '):
        for key in dic:
            for i in range(0, len(funcion_fu)):
                dic[key]["If/elif"] = funcion_fu[i].count("if") + funcion_fu[i].count("elif")
        funcion_fu = leer_archivo(ar_fuente)
    ar_fuente.close()
    return dic
    
ar_fuente = open('fuente_unico1.csv', 'r')
diccionario = organizar_archivo(ar_fuente)
print(if_elif(ar_fuente, diccionario))
ar_fuente.close()