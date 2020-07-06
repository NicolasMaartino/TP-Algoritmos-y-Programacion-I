#!/usr/bin/env python3
'''def contar_sentencias(lista_codigo):
    cont_if = 0
    cont_for = 0
    cont_while = 0
    cont_return = 0
    cont_elif = 0
    for codigo in lista_codigo:
        print(codigo)
        if 'if' in codigo:
            cont_if += 1
        elif 'for' in codigo:
            cont_for += 1
        elif 'while' in codigo:
            cont_while += 1
        elif 'return' in codigo:
            cont_return += 1
        elif 'elif' in codigo:
            cont_elif += 1
    return cont_if, cont_for,cont_while, cont_return, cont_elif PARA DESPUES AMEO'''



def archivo_lista(lista_codigo,lista_codigo_2):
    lista_codigo_ordenado = sorted(lista_codigo)
    lista_codigo_2_ordenado = sorted(lista_codigo_2)
    

def leer_rutas(archivo):
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip('\n') 
    else:
        devolver = ""
    return devolver

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
        archivo_lista(lista_codigo[0:pos],lista_codigo[pos:])
    




listar_archivo()