#!/usr/bin/env python3
import csv
from os import remove
from generales import buscar_dato,unir_linea,reemplazar_toda_la_lista,reemplazar_string,ordenamiento_insercion,leer_archivo,tipo_archivos 
from archivos import *

def guarda_archivo_mezcla (archivo_aux,lista_archivos):
    """ Autor : Alejandro"""
    """ Ayuda : Lee archivo_aux.csv, extrae la informacion y realiza la mezcla respectiva para luego eliminar archivo_aux.csv"""
    archivo_mezcla = tipo_archivos(lista_archivos[0])
    with open(archivo_mezcla,"w") as prestaciones:
        with open(archivo_aux,"r") as auxiliar:
            entrada = csv.reader(auxiliar)
            ordenado = sorted(entrada, key=lambda fila: fila[0])
            for fila in ordenado:
                salida = csv.writer(prestaciones)
                salida.writerow(fila)
    remove(archivo_aux) 

def mezcla (lista_archivos):
    """ Autor : Alejandro """
    """ Ayuda : Mezcla Archivos CSV's """
    archivo_aux = "archivo_aux.csv"
    with open(archivo_aux,"w") as unificado:
        for archivo in lista_archivos:
            with open(archivo,'r') as arch:
                linea = leer_archivo(arch)
                while linea:
                    entrada = csv.writer(unificado)
                    entrada.writerow(linea)
                    linea = leer_archivo(arch)
    guarda_archivo_mezcla(archivo_aux,lista_archivos)

def separa_comentarios_fuentes (lista_archivos):
    """ Autor : Alejandro"""
    """ Ayuda : Esta función recibe una lista con comentarios y fuente, divide en dos listas acorde al nombre respectivo"""
    comentarios = []
    fuente_unico = []
    for ruta in lista_archivos:
        if "comentarios" in ruta:
            comentarios.append(ruta)
        else:
            fuente_unico.append(ruta)
    mezcla(comentarios)
    mezcla(fuente_unico)

def linea_ayuda_autor (linea,linea_comentarios,linea_fuente,palabras_buscadas):
    """[Autor : Nicolas] """
    """[Ayuda : Se le pasa una lista con las palabras encontradas y se fija si realmente alguna esta]"""
    
    encontro = False
    i = 0
    
    while i<len(palabras_buscadas) and encontro == False:
        
        if palabras_buscadas[i] == "Autor":
            encontro = True
            union=reemplazar_toda_la_lista(linea,['"""','[',']',"Autor",":"],"")
            union = unir_linea(union," ").strip()
            linea_comentarios.insert(1,union)
        
        elif palabras_buscadas[i] == "Ayuda":
            encontro = True
            union= reemplazar_toda_la_lista(linea,['"""','[',']',"Ayuda",":"],"")
            union = unir_linea(union," ").strip()
            linea_comentarios.insert(2,union)
        
        elif palabras_buscadas[i] == "#":
            encontro = True
            linea_fuente,linea_comentarios=seccion_comentarios(linea,linea_comentarios,linea_fuente)
        
        i+=1
    
    return encontro,linea_fuente,linea_comentarios

def validar_linea (nombre_modulo,archivo) :
    """[Autor : Nicolas]"""
    """[Ayuda : Va a validar las lineas del archivo para saber 
        a cual de las dos salidas (comentarios y fuente unico) va a ir]"""
    funciones_fuente = [] # Aca iran a parar las funciones para fuente codigo 
    funciones_comentarios = [] # Y aca las funciones para comentarios
    ultima_lectura = leer_linea(archivo)
    while ultima_lectura[0] != '""""""':
        if ultima_lectura[0] == "def":
            #Analizaremos la funcion y la dividiremos en dos listas para saber a que archivo pertenecen.
            nombre_funcion = ultima_lectura[1]
            parametros = reemplazar_string(","," ",ultima_lectura[2])
            linea_fuente = [nombre_funcion,parametros,nombre_modulo]
            linea_comentarios = [nombre_funcion] 
            linea_comentarios,linea_fuente,ultima_lectura=analizo_funcion(linea_fuente,linea_comentarios,archivo)
            funciones_fuente.append(linea_fuente)
            funciones_comentarios.append(linea_comentarios)
        else:
            ultima_lectura=leer_linea(archivo)
    
    return ordenamiento_insercion(funciones_fuente),ordenamiento_insercion(funciones_comentarios)
def analizo_funcion (linea_fuente,linea_comentarios,archivo):
    """[Autor : Nicolas ] """
    """[Ayuda : Analizara la funcion para enviarla a las listas correspondientes]"""
    
    lectura=leer_linea(archivo)
    
    while lectura[0] != "def" and lectura[0]!='""""""':
        lectura = reemplazar_toda_la_lista(lectura,[',']," ")
        lectura = reemplazar_toda_la_lista(lectura,['"""',"[","]"],"")
        encontradas = buscar_dato(["Ayuda","Autor","#"],lectura)
        encontro,linea_fuente,linea_comentarios = linea_ayuda_autor(lectura,linea_comentarios,linea_fuente,encontradas)
        
        if encontro == False and lectura[0]:
            linea_fuente.append(unir_linea(lectura," "))
        
        lectura = leer_linea(archivo)
    
    return linea_comentarios,linea_fuente,lectura

def seccion_comentarios (lectura,lista_comentarios,lista_fuente) :
    """[Autor : Nicolas] """
    """[Ayuda : Este es el sector que corresponderia al analisis de la linea del archivo que corresponde a comentarios] """
    
    i = 0
    encontro = False # Esto es condición para que cuando encuentre la almohadilla salga del while
    
    while i<len(lectura) and encontro == False:
        elemento = lectura[i]
        
        if elemento == "#" and i>0 :
            encontro = True
            comentario = lectura[i:len(lectura)]
            fuente_unico = lectura[0:i]
            lista_fuente.append(unir_linea(fuente_unico," "))
            lista_comentarios.append(unir_linea(comentario," "))
        
        elif elemento == "#" and i==0 :
            encontro = True
            lista_comentarios.append(unir_linea(lectura," "))
        i+=1
    
    return lista_fuente,lista_comentarios
def analiza_codigo () :
    """[ Autor : Nicolas]"""
    """[Ayuda : Guardara codigo como lo pide el enunciado]"""
    
    # Esta funcion guardará cada archivo ordenado en una lista
    
    lista_archivos = []
    rutas = open("programas.txt", 'r')
    ruta = leer_linea_string(rutas)
    i = 0
    while ruta: # aaj
        i+=1 # Este indice lo creo para distinguir los archivos
        nombre_archivo = ruta.split("/").pop()
        
        # Abro ruta dentro de programas.txt
        codigo = open(ruta,'r')
        fuente_unico,comentarios = validar_linea(nombre_archivo,codigo)
        ruta_fuente = "fuente_unico"+str(i) +".csv"
        ruta_comentarios= "comentarios"+str(i) +".csv"
        generar_archivo(fuente_unico,ruta_fuente)
        generar_archivo(comentarios,ruta_comentarios)
        lista_archivos.append(ruta_fuente)
        lista_archivos.append(ruta_comentarios)
        ruta = leer_linea_string(rutas)
    separa_comentarios_fuentes(lista_archivos)
    return lista_archivos

analiza_codigo()
""""""
