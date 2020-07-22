#!/usr/bin/env python3
from archivos import leer_linea_clasico,buscar_funciones
from tabla import formato_interrogacion,formato_numeral,imprimir_todo,tabla_consultas

def opcion_todo (nombre, archivo_funciones, archivo_comentarios):
    """[Autor: Juan Godoy]"""
    """[Ayuda : Funcion que imprime todo lo relacionado con las funciones ?todo, #todo,e imprimir ?todo]"""
    ayuda_funciones=open("ayuda_funciones.txt", "w") 
    archivo_funciones.seek(0)
    archivo_comentarios.seek(0)
    
    lista_funciones=leer_linea_clasico(archivo_funciones, ",")
    lista_comentarios=leer_linea_clasico(archivo_comentarios, ",")
    while lista_funciones[0]!="":
        if nombre == "?todo":
            formato_interrogacion(lista_funciones, lista_comentarios)
        elif nombre=="imprimir ?todo":
            imprimir_todo(ayuda_funciones, lista_funciones, lista_comentarios)
        else:
            formato_numeral(lista_funciones, lista_comentarios)
        lista_comentarios = leer_linea_clasico(archivo_comentarios, ",")
        lista_funciones = leer_linea_clasico(archivo_funciones, ",")
    ayuda_funciones.close()
    return 
    

def opciones_funcion(valor, archivo_funciones, archivo_comentarios):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Segun la opcion que se elija, se imprime diferente informacion sobre las funciones]"""

    if valor == "?todo" or valor == "#todo" or valor =="imprimir ?todo":
        opcion_todo (valor, archivo_funciones, archivo_comentarios)
    else:
        nombre_funcion=valor.replace(valor[-1], "")
        
        archivo_comentarios.seek(0)
        archivo_funciones.seek(0)
        
        lista_comentarios = buscar_funciones(archivo_comentarios, nombre_funcion)
        lista_funciones = buscar_funciones(archivo_funciones, nombre_funcion)
        
        if (valor.endswith("?")) and (lista_comentarios[0]!="") and (lista_funciones[0]!=""):
            formato_interrogacion(lista_funciones, lista_comentarios)
        elif (valor.endswith("#")) and (lista_comentarios[0]!="") and (lista_funciones[0]!=""):
            formato_numeral(lista_funciones, lista_comentarios)
        else:
            print("\nPorfavor ingrese un nombre de funcion valido seguido de ? o #. \n")
    return 
        
        
def panel_consultas(fuente_unico, comentarios):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Funcion principal que pide el ingreso de una funcion y segun la opcion que elijas, imprime diversas cosas]"""
    
    tabla_consultas(comentarios)
    valor_solicitado=input("\nFunción: ")
    while valor_solicitado:
        if valor_solicitado=="imprimir ?todo" or valor_solicitado=="?todo" or valor_solicitado=="#todo":
            opcion_todo(valor_solicitado, fuente_unico, comentarios)
        else:
            opciones_funcion(valor_solicitado,fuente_unico, comentarios)
        valor_solicitado=input("\nFunción: ")



    

    

