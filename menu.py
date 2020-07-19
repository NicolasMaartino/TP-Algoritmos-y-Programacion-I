#!/usr/bin/env python3
from merge import analiza_codigo
from archivos import abrir_archivos
from panel_general_de_funciones import panel_general
from informacion_desarrollador import informacion_desarrolladores
from reutilizacion_codigo import imprimir_analizador
from generales import validacion_archivo_programas


def menu():
    """ [Autor : N/N]
        [Ayuda : Menu principal de nuestro programa]"""
    
    
    """ Esta es la funcion de menu principal de nuestro programa.
        Todo estara ejecutado desde aca.
    """
    vacio=validacion_archivo_programas()
    if vacio!=True:
        analiza_codigo()
        fuente_codigo = abrir_archivos("fuente_unico.csv","r")
        comentarios = abrir_archivos("comentarios.csv","r")
        texto_menu()
        opcion = ingresar("Ingrese opción: ")
        while opcion:
            if opcion=="1":
                panel_general(fuente_codigo,comentarios)
            elif opcion=="2":
                pass
                #funcion_2()
            elif opcion=="3":
                imprimir_analizador()
            elif opcion=="4":
                pass
                #funcion_4()
            elif opcion=="5":
                informacion_desarrolladores()
            texto_menu()
            opcion=ingresar("Ingrese una opción o en blanco para salir: ")
    else:
        print("\n\t\tATENCION [!]\n\n\tProgramas.txt ESTA VACIO\n")

def texto_menu():
    print("""            1- Panel general de funciones
            2-Consulta de funciones
            3-Analizador de reutilización de código
            4-Árbol de invocación
            5-Información por desarrollador""")

def ingresar(leyenda):
    return input(leyenda)


menu()
