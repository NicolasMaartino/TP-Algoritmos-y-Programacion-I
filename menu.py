#!/usr/bin/env python3
from merge import analiza_codigo
from archivos import abrir_archivos
from panel_general_de_funciones import panel_general
from informacion_desarrollador import informacion_desarrolladores
from reutilizacion_codigo import imprimir_analizador
from generales import validacion_archivo_programas
from panelConsulta import panel_consultas
<<<<<<< HEAD

def texto_menu():
    print("""            1- Panel general de funciones
            2-Consulta de funciones
            3-Analizador de reutilización de código
            4-Árbol de invocación
            5-Información por desarrollador""")

def ingresar(leyenda):
    return input(leyenda)

=======
import os
>>>>>>> 0b03654256ae6e48cb23e9957916c7410054b17b

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
        opcion =input("Ingrese una opcion: ")
        while opcion:
            os.system("clear")
            while opcion not in "12345":
                texto_menu()
                opcion=input("Ingrese una opcion valida o enter para salir: ")
            if opcion == "":
                print("Gracias por participar de nuestro programa")
                exit()
            elif opcion=="1":
                panel_general(fuente_codigo,comentarios)
                enter = input("Ingrese enter para continuar")
            elif opcion=="2":
<<<<<<< HEAD
                panel_consultas(fuente_codigo, comentarios)
=======
                panel_consultas(fuente_codigo, comentarios) 
>>>>>>> 0b03654256ae6e48cb23e9957916c7410054b17b
            elif opcion=="3":
                imprimir_analizador()
                enter = input("Ingrese enter para continuar")
            elif opcion=="4":
                pass
                #funcion_4()
            elif opcion=="5":
                informacion_desarrolladores()
                enter = input("Ingrese enter para continuar")
            os.system("clear")
            texto_menu()
            opcion=ingresar("Ingrese una opción o en blanco para salir: ")
    else:
        print("\n\t\tATENCION [!]\n\n\tProgramas.txt ESTA VACIO\n")

<<<<<<< HEAD
menu()

""""""
=======
def texto_menu():
    print("""            1- Panel general de funciones
            2-Consulta de funciones
            3-Analizador de reutilización de código
            4-Árbol de invocación
            5-Información por desarrollador""")

def ingresar(leyenda):
    return input(leyenda)
>>>>>>> 0b03654256ae6e48cb23e9957916c7410054b17b
