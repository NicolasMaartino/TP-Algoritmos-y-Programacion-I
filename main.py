def menu():
    texto_menu()
    opcion=ingresar("Ingrese opción: ")
    while opcion:
        if opcion=="1":
            pass
            #funcion_1()
        elif opcion=="2":
            pass
            #funcion_2()
        elif opcion=="3":
            pass
            #funcion_3()
        elif opcion=="4":
            pass
            #funcion_4()
        elif opcion=="5":
            pass
            #funcion_5()
        texto_menu()
        opcion=ingresar("Ingrese una opción o en blanco para salir: ")

def texto_menu():
    print("""            1- Panel general de funciones
            2-Consulta de funciones
            3-Analizador de reutilización de código
            4-Árbol de invocación
            5-Información por desarrollador""")


def ingresar(leyenda):
    return input(leyenda)


menu()
