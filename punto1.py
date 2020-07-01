#!/usr/bin/env python3
import os
minimo=0
def convertir_linea_iterable(archivo,condicion_corte):
    linea = leer_linea_string(archivo)
    if linea:
        devolver = linea.split(condicion_corte)
    else:
        devolver = minimo
    return devolver
def leer_linea_string(archivo):
    #Esta función lee el archivo pero no lo convierte en iterable
    return archivo.readline().rstrip("\n") 
def guarda_codigo():
    #Esta funcion guardará cada archivo ordenado en una lista
    lista_archivos=[]
    with open("programas.txt", 'r') as programa:
        linea = leer_linea_string(programa)
        while linea:
            with open(linea,'r') as codigo:
                archivo_ordenado=ordenar_archivo(codigo)
                lista_archivos.append(archivo_ordenado)
            linea = leer_linea_string(programa)
    return lista_archivos
def merge(lista_archivos):
    cantidad_archivos=len(lista_archivos)
    y=0
    for x in range (cantidad_archivos):











def cargar_memoria_archivo(archivo):
    #Esta funcion convierte el archivo entero en un iterable
    linea=leer_linea_string(archivo).strip()
    archivo_cargado=[]
    while linea:
        archivo_cargado.append(linea)
        linea=leer_linea_string(archivo).strip()
    return archivo_cargado
def ordenar_archivo(archivo):
    #Esta función ordena el archivo
    archivo_cargado=cargar_memoria_archivo(archivo)
    archivo_ordenado=sorted(archivo_cargado)
    return archivo_ordenado

                    


print(guarda_codigo())




