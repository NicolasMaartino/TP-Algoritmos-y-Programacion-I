from archivos import leer_linea
archivo = open("main.py","r",newline="\n")

def funcion(archivo):
    linea = leer_linea(archivo," ")
    while linea:
        print("Detecta linea",linea)
        linea = leer_linea(archivo," ")

funcion(archivo)

