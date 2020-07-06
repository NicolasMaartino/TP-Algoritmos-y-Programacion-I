#!/usr/bin/env python3

def leer_rutas(archivo):
    """
    leer el archivo programas.txt
    """
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip('\n') 
    else:
        devolver = ""
    return devolver

def grabar_nuevo(archivoentero,linea_cod_general):
    archivoentero.write(linea_cod_general+'\n')

def mezcla():
    with open("archivo1.txt") as archivo1, open("archivo2.txt") as archivo2, open('archivoentero.txt','w') as archivoentero:
        linea_cod1 = leer_rutas(archivo1)
        linea_cod2 = leer_rutas(archivo2)
        while linea_cod1 and linea_cod2:
            if linea_cod1 ==  linea_cod2:
                grabar_nuevo(archivoentero,linea_cod1)
                grabar_nuevo(archivoentero,linea_cod2)
                linea_cod1 = leer_rutas(archivo1)
                linea_cod2 = leer_rutas(archivo2)
            elif linea_cod1[:1]<linea_cod2[:1]:
                grabar_nuevo(archivoentero,linea_cod1)
                linea_cod1 = leer_rutas(archivo1)
            else:#linea_cod1[:1]>linea_cod2[:1]:
                grabar_nuevo(archivoentero,linea_cod2)
                linea_cod2 = leer_rutas(archivo2)


def crear_archivos_ordenados(l_codigo1,l_codigo2):
    """"
    Recibe dos listas para luego ordenarlas y finalmente cargarlas en dos archivos
    """
    l_codigo_ordenado = sorted(l_codigo1)
    l_codigo2_ordenado = sorted(l_codigo2)
    with open('archivo1.txt','w') as archivo1, open('archivo2.txt','w') as archivo2:
        for linea1,linea2 in zip(l_codigo_ordenado,l_codigo2_ordenado):
            if linea1 != ''and linea2 != '':
                archivo1.write(linea1+'\n')
                archivo2.write(linea2+'\n')


def listar_archivo():
    lista_codigo = []
    lista_posiciones = []
    with open('programas.txt','r') as programa:
        ruta = leer_rutas(programa)
        while ruta:
            with open(ruta,'r') as codigo:
                linea_codigo = codigo.readline()
                lista_codigo.append(ruta)
                while linea_codigo:
                    lista_codigo.append(linea_codigo.strip()) 
                    linea_codigo = codigo.readline()
            pos = lista_codigo.index(ruta)
            ruta = leer_rutas(programa)
        crear_archivos_ordenados(lista_codigo[0:pos],lista_codigo[pos:])
    




listar_archivo()
mezcla()