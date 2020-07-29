#!/usr/bin/env python3
def leo_archivo(archivo):
    """
    Autor : Sofia Marchesini
    Ayuda : Esta funcion lee el archivo linea por linea y
    devuelve una lista de los elementos separados por coma
    """
    
    linea = archivo.readline()
    linea = linea.rstrip().split(',')
    return linea


def lista_de_funciones(fuente):
    """
    Autor : Sofia Marchesini
    Ayuda : Esta funcion crea una lista de funciones compuesta por
    los nombres de todas las funciones que se encuentran
    en el primer elemento de las lineas del archivo 
    """
    
    fuente = open("fuente_unico.csv", 'rt')
    linea = leo_archivo(fuente)
    funciones = []
    
    while linea[0]:
        funciones.append(linea[0])
        linea = leo_archivo(fuente)
    fuente.close()
    
    return funciones


def veces_invocaciones(linea):
    """
    Autor : Sofia Marchesini
    Ayuda : esta funcion crea un dicionario compuesto por
    la clave como la funcion invocada y el valor
    como las veces que esta funcion fue invocada
    """
    
    funciones = lista_de_funciones(fuente)
    veces_invocadas = {}
    for funcion in funciones:
        for palabras in linea[3:-1]:
            if funcion in palabras and funcion not in veces_invocadas:
                veces_invocadas[funcion] = 1
            elif funcion in palabras and funcion in veces_invocadas:
                veces_invocadas[funcion] += 1
    
    return veces_invocadas

def funciones_invocadas(fuente):
    """
    Autor : Sofia Marchesini
    Ayuda: esta funcion crea un diccionario con todas las funciones como claves.
    El diccionario tendra como valor como un diccionario compuesto por la funcion
    que invoco , y el valor las veces invocada.
    Si no invoca ninguna funcion aparecera la lista vacia
    """
    #funcion1 {funcion2 : n veces} , funcion 1 llama a funcion 2 n veces
    

    linea = leo_archivo(fuente)
    invocaciones = {}

    while linea[0]:
        funcion_1 = linea[0]        
        invocaciones[funcion_1] = veces_invocaciones(linea)
        linea = leo_archivo(fuente)
    fuente.close()
    return invocaciones


def tabla_0(invocaciones, funciones):
    """
    Autor : Sofia Marchesini
    Ayuda : Empiezo la primera parte de crear la tabla
    
    #funcion1 {funcion2 : n veces} , funcion 1 llama a funcion 2 n veces}
    n ) la funcion de la fila invoca n veces a la funcion de la columna
    x ) la funcion de la columna invoca a la funcion de la fila
    
    empezamos con la x
    recorremos todas las funciones de las filas
    nos paramos en la funcion 1:
    si funcion 1(va ir variando) en valores de funcion1 (no varia hasta recorrer todas las funciones en la funcion 1):
       agrego una  x en la fila de funcion 1 y columna de funcion1
    si funcion 1 no en valores de funcion 1:
    agrego vacio
       
    ahora con la cantidad n
    recorremos todas las funciones de las filas
    si 
    agrego la cantidad de veces equivalente a esa funcion"""

    filas = ""
    total = {}
    
    for x in range(1,len(funciones)+1):
        for func_llama in invocaciones:
            if funciones[x-1] in invocaciones[func_llama]: 
                filas += "|{:^5}|".format("x")
            elif func_llama in invocaciones[funciones[x-1]]:
                filas += "|{:^5}|".format(invocaciones[funciones[x-1]][func_llama])
                total[func_llama] += invocaciones[funciones[x-1]][func_llama]
        
            else:
                filas += "|{:^5}|".format("")
                
    return filas,total

def tabla(funciones):
    i = 0
    cadena = ''
    linea = '-'*40
    print('\t\tFunciones')
    print(linea)
    for invocacion in funciones.keys():
        i += 1
        l_num = [str(x) for x in funciones[invocacion].values()]
        print("|{0:0}-{1:<8}|\t{2:>8}|".format(i,invocacion,"|".join(l_num)))
fuente = open("fuente_unico.csv", 'rt')
funciones = funciones_invocadas(fuente)
tabla(funciones)