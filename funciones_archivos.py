#!/usr/bin/env python3
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
    return archivo.readline().strip() 
def guarda_codigo():
    #Esta funcion guardará cada archivo ordenado en una lista
    lista_archivos=[]
    with open("programas.txt", 'r') as programa:
        linea = leer_linea_string(programa)
        while linea:
            with open(linea,'r') as codigo:
                codigo_iterable=cargar_memoria_archivo(codigo)
                lista_archivos.append(codigo_iterable)
            linea = leer_linea_string(programa)
        archivo_completo=open("archivo.txt","w")
        iterable_completo=merge(lista_archivos,archivo_completo)
        pasar_lista_a_archivo(iterable_completo,archivo_completo)

        #funcion q analize el archivo y de como salida los otros 2 archivos!
        #funcion()

    return lista_archivos
def pasar_lista_a_archivo(lista,archivo):
    for linea in lista:
        escribir_linea(linea,archivo)

def merge(lista_archivos,archivo_completo):
    cantidad_archivos=len(lista_archivos)
    lista_final=[]
    for archivo in lista_archivos:
        lista_final.extend(archivo)
    iterable_ordenado=ordenamiento_insercion(lista_final)
    return iterable_ordenado
    
def escribir_linea(linea,archivo):
    #Escribe una linea
    leyenda=linea+"\n"
    archivo.write(leyenda)

def cargar_memoria_archivo(archivo):
    #Esta funcion convierte el archivo entero en un iterable
    linea=leer_linea_string(archivo)
    archivo_cargado=[]
    while linea:
        archivo_cargado.append(linea)
        linea=leer_linea_string(archivo)
    return archivo_cargado

def ordenar_archivo(iterable):
    #Esta función ordena el archivo
    iterable_ordenado=sorted(iterable)
    return iterable_ordenado

def ordenamiento_insercion(lista):
    for indice in range(1,len(lista)):
        valor=lista[indice]
        i=indice-1
        variable=True
        while i>=0 and variable==True:
            if valor<lista[i]:
                lista[i+1]=lista[i]
                lista[i]=valor

                i=i-1
            else:
                variable=False
    return lista
                    


guarda_codigo()




