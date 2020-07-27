from reutilizacion import funciones_invocadas, crear_filas 
from generales import listar_archivo
from archivos import leer_linea_clasico

def busca_main(dic):
    """[Autor: Sofia y Lucia]"""
<<<<<<< HEAD
    """[Ayuda: Busca funciones que sea la función principal]"""       
=======
    """[Ayuda: Busca la función principal]"""
           
>>>>>>> 10f83d7daf47b6618683dee8f6749ed686687054
    main = ""   
    valores = list(dic.values())
    contador = 0
    for key in dic.keys():
        while (len(valores) > contador) and (key not in list(valores[contador].keys())):
            main = key
            contador += 1   
    return main


def cant_lineas(lista_ar_fu):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de lineas por funcion]"""
    
    dic = {}
    for funcion in lista_ar_fu:
        dic[funcion[0]] = (len(funcion) - 2)
        
    return dic

def imprimir_diagrama():
<<<<<<< HEAD
    """[Autor : Sofia Marchesini]"""
    """[Ayuda : este codigo permite imprimir las funciones main
     con sus respectivas funciones invocadas y las funciones que a su vez
     estas invocan y asi sucesivamente]"""
    
    fuente_unico = open("fuente_unico.csv", "r")
=======
    
    """[Autor : Sofia Marchesini]"""
    """[Ayuda : este codigo permite imprimir las funciones main
        con sus respectivas funciones invocadas y las funciones que a su vez
        estas invocan y asi sucesivamente]"""
        
    fuente_unico = open("fuente_unico.csv","r")
>>>>>>> 10f83d7daf47b6618683dee8f6749ed686687054
    lista_ar = listar_archivo(fuente_unico)
    fuente_unico.close()
    fuente_unico = open("fuente_unico.csv","r")
    diccionario = funciones_invocadas(fuente_unico)
    dic_lineas = cant_lineas(lista_ar)
<<<<<<< HEAD
    main=busca_main(diccionario)

=======
    main = busca_main(diccionario)       
    
>>>>>>> 10f83d7daf47b6618683dee8f6749ed686687054
    print("{}({}) ".format(main,dic_lineas[main]),end = "")
    for key in diccionario[main].keys():
        if key:
            print("---> {}({}) ".format(key,dic_lineas[key]),end="")
            for value in diccionario[key].keys():
<<<<<<< HEAD
                if value != key:
                    print("")
                    print("\t---> {}({})".format(value,dic_lineas[value]), end = "")
            print("\n")
=======
                print(" ---> {}({})".format(value,dic_lineas[value]), end = "")
            print("\n")
            
>>>>>>> 10f83d7daf47b6618683dee8f6749ed686687054
