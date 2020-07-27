from reutilizacion import funciones_invocadas, crear_filas 
from generales import listar_archivo

def busca_main(dic):
    """[Autor: Sofia y Lucia]"""
    """[Ayuda: Busca la función principal]"""
           
    main = ""   
    valores = list(dic.values())
    for key in dic.keys():
        contador = 0
        while (len(valores) > contador) and (key not in list(valores[contador].keys())):
            if (contador == len(valores) - 1):
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
=======
    """
    [Autor : Sofia Marchesini]
    [Ayuda : este codigo permite imprimir las funciones main
     con sus respectivas funciones invocadas y las funciones que a su vez
     estas invocan y asi sucesivamente]"""
>>>>>>> 49e2ebdf92307134008d6d8a34e1649d04d96483
        
    fuente_unico = open("fuente_unico.csv","r")
    lista_ar = listar_archivo(fuente_unico)
    fuente_unico.close()
    fuente_unico = open("fuente_unico.csv","r")
    diccionario = funciones_invocadas(fuente_unico)
    dic_lineas = cant_lineas(lista_ar)
    main = busca_main(diccionario)       
    
    print("{}({}) ".format(main,dic_lineas[main]),end = "")
    for key in diccionario[main].keys():
        if key != "":
            print(" ---> {}({}) ".format(key,dic_lineas[key]),end = "")
            for value in diccionario[key].keys():
                print(" ---> {}({})".format(value,dic_lineas[value]), end = "")
<<<<<<< HEAD
            print("\n")
            
               
=======
            print("\n")               
>>>>>>> 49e2ebdf92307134008d6d8a34e1649d04d96483
