#!/usr/bin/env python3
import csv
import codecs
from os import remove
from generales import buscar_dato,unir_linea,reemplazar_toda_la_lista,reemplazar_string,ordenamiento_insercion,tipo_archivos,item_necesario,agregar_linea_especifica
from archivos import *

def guarda_archivo_mezcla(archivo_aux, lista_archivos):
    """[Autor : Alejandro] 
     Ayuda : Lee archivo_aux.csv, extrae la informacion y realiza la mezcla respectiva 
     para luego eliminar archivo_aux.csv 
     """
    archivo_mezcla = tipo_archivos(lista_archivos[0])
    with open(archivo_mezcla,"w") as prestaciones:
        with open(archivo_aux,"r") as auxiliar:
            entrada = csv.reader(auxiliar)
            ordenado = sorted(entrada, key=lambda fila: fila[0])
            for fila in ordenado:
                salida = csv.writer(prestaciones)
                salida.writerow(fila)
    remove(archivo_aux) 

def mezcla(lista_archivos):
    """[Autor : Alejandro] """
    """[Ayuda : Mezcla Archivos CSV's] """
    archivo_aux = "archivo_aux.csv"
    with open(archivo_aux,"w") as unificado:
        for archivo in lista_archivos:
            with open(archivo,'r') as arch:
                linea = leer_linea(arch)
                while linea:
                    entrada = csv.writer(unificado)
                    entrada.writerow(linea)
                    linea = leer_linea(arch)
    guarda_archivo_mezcla(archivo_aux,lista_archivos)

def separa_comentarios_fuentes(lista_archivos):
    """ Autor : Alejandro """
    """ Ayuda : Esta función recibe una lista con comentarios y fuente, divide en dos listas acorde al nombre respectivo """
    comentarios = []
    fuente_unico = []
    
    for ruta in lista_archivos:
        if "comentarios" in ruta:
            comentarios.append(ruta)
        else:
            fuente_unico.append(ruta)    
    mezcla(comentarios)
    mezcla(fuente_unico)

def indice_lista_vacia(lista_datos, lista_borrar):
    """[Autor : Nicolas]
        Ayuda : Esta funcion recibira una lista con datos que podra
            ir borrando y cuando este vacia devolvera el indice donde se
            vacio por completo. 
    """
    i=0
    while i<len(lista_datos) and len(lista_borrar)>0:
        if lista_datos[i] in lista_borrar:
            lista_borrar.remove(lista_datos[i])
        i+=1
    return i

def linea_ayuda_autor(linea, linea_comentarios , linea_fuente,palabras_buscadas,palabras_faltantes):
    """ [Autor : Nicolas] """
    """ [Ayuda : Se le pasa una lista con las palabras encontradas y se fija si realmente alguna esta] """        
    
    if "Autor" in palabras_buscadas and "Ayuda" in palabras_buscadas:
        palabras_faltantes.append("Autor")
        palabras_faltantes.append("Ayuda")
        i = indice_lista_vacia(linea,["Ayuda","Autor"])
        linea_segunda=linea[i-1:len(linea)]
        linea_primera = linea[0:i-1]
        linea_primera = reemplazar_toda_la_lista(linea_primera,["Autor","Ayuda",'"""',","],"")
        linea_segunda = reemplazar_toda_la_lista(linea_segunda,["Autor","Ayuda",'"""',","],"")
        linea_comentarios = agregar_linea_especifica(1,linea_primera,linea_comentarios)
        linea_comentarios = agregar_linea_especifica(2,linea_segunda,linea_comentarios)
    elif "Autor" in palabras_buscadas :
        palabras_faltantes.append("Autor")
        union=reemplazar_toda_la_lista(linea,['"""','[',']',"Autor",":"],"")
        linea_comentarios = agregar_linea_especifica(1,union,linea_comentarios)
    elif "Ayuda" in palabras_buscadas:
        palabras_faltantes.append("Ayuda")
        union= reemplazar_toda_la_lista(linea,['"""','[',']',"Ayuda",":"],"")
        linea_comentarios = agregar_linea_especifica(2,union,linea_comentarios)
    elif "#" in palabras_buscadas or '"""' in palabras_buscadas:
        linea_fuente,linea_comentarios=seccion_comentarios(linea,linea_comentarios,linea_fuente)
    
    return linea_fuente,linea_comentarios,palabras_faltantes

def reunir_parametros(linea):
    """ [Autor : Nicolas] """
    """ [Ayuda : reune parametros ja 
        """

    nueva_lista=[]
    for x in range (2,len(linea)):
        nueva_lista.extend([linea[x]])
    nueva_lista=item_necesario(nueva_lista,","," ")
    final = unir_linea(nueva_lista," ")
    return final
            

            
def validar_linea(nombre_modulo, archivo) :
    """ [Autor : Nicolas] """
    """ [Ayuda : Va a validar las lineas del archivo para saber 
        a cual de las dos salidas (comentarios y fuente unico) va a ir] 
        """
    funciones_fuente = [] # Aca iran a parar las funciones para fuente codigo 
    funciones_comentarios = [] # Y aca las funciones para comentarios
    ultima_lectura = leer_linea(archivo)
    while ultima_lectura:
        if "def" in (ultima_lectura[0]).strip():
            # Analizaremos la funcion y la dividiremos en dos listas para saber a que archivo pertenecen.
            ultima_lectura = item_necesario(ultima_lectura,"("," (")
            ultima_lectura = item_necesario(ultima_lectura,":","")
            parametros = reunir_parametros(ultima_lectura)
            nombre_funcion = ultima_lectura[1]
            parametros = reemplazar_string(","," ",parametros)
            linea_fuente = [nombre_funcion,parametros,nombre_modulo]
            linea_comentarios = [nombre_funcion]
            linea_comentarios,linea_fuente,ultima_lectura = analizo_funcion(linea_fuente,linea_comentarios,archivo)
            funciones_fuente.append(linea_fuente)
            funciones_comentarios.append(linea_comentarios)
        else:#Si no es un def no es una funcion.Probablemente sea un from o un bloque principal.El enunciado no pide analizarlo.
            ultima_lectura=leer_linea(archivo)
    return ordenamiento_insercion(funciones_fuente),ordenamiento_insercion(funciones_comentarios)

def analizo_funcion(linea_fuente,linea_comentarios,archivo):
    """
    [Autor : Nicolas ] 
    """
    """[Ayuda : Analizara la funcion para enviarla a las listas correspondientes] """

    lectura = leer_linea(archivo)
    
    #Si sale de este while, esta por empezar otra funcion o leyo el fin de archivo.
    
    palabras_faltantes = []

    while ("def" in (lectura[0]).strip()) and lectura:
        lectura = reemplazar_toda_la_lista(lectura,[","]," ")
        #Las comas molestan en la lectura del archivo. Las eliminamos y ponemos un espacio en su lugar.
        lectura = item_necesario(lectura,"]"," ")
        lectura = item_necesario(lectura,"["," ")
        lectura = item_necesario(lectura,"#","# ")
        #Esta funcion es clave, me simplifica la lectura de las lineas.
        cuento = lectura.count('"""')
        """ 
        Preguntare si abrio una triple comillas 
        y nunca lo cerro. Eso nos estaria diciendo que el comentario
        no finalizo.
        """
        while cuento == 1:
            """
            Guarda aca, el codigo esta preparado para detectar un corchete para separar
            de la triple comilla y en caso de que no haya corchete dejar un 
            espacio antes de la triple comilla.
            """
            segunda_lectura=leer_linea(archivo)
            segunda_lectura = item_necesario(segunda_lectura,"]"," ")
            segunda_lectura = item_necesario(segunda_lectura,"["," ")
            lectura.extend(segunda_lectura)
            cuento = lectura.count('"""')
        lectura = reemplazar_toda_la_lista(lectura,["[","]",":"],"")
        encontradas = buscar_dato(["Ayuda","Autor","#",'"""'],lectura)
        linea_fuente,linea_comentarios,palabras_faltantes = linea_ayuda_autor(lectura,linea_comentarios,linea_fuente,encontradas,palabras_faltantes)
        if len(encontradas) == 0 and lectura:
            linea_fuente.append(unir_linea(lectura," "))
        lectura = leer_linea(archivo)
    linea_comentarios =hay_autor_ayuda(palabras_faltantes,linea_comentarios)
    
    return linea_comentarios,linea_fuente,lectura

def detectar_autor_ayuda(palabras_encontradas, palabras_faltantes):
    if "Autor" in palabras_encontradas:
        palabras_faltantes.append("Autor")
    elif "Ayuda" in palabras_encontradas:
        palabras_faltantes.append("Ayuda")
    return palabras_faltantes

def hay_autor_ayuda(palabras,linea_comentarios):
    if "Autor" not in palabras:
        linea_comentarios.insert(1,"N/N")
    if "Ayuda" not in palabras:
        linea_comentarios.insert(2,"N/N")
    return linea_comentarios

def seccion_comentarios(lectura, lista_comentarios, lista_fuente) :
    """ [ Autor : Nicolas] """
    """
        [Ayuda : Este es el sector que corresponderia al analisis de la linea del archivo 
            que corresponde a comentarios]
    """
    
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
        elif elemento == '"""':
            lectura = reemplazar_toda_la_lista(lectura,['"""'],"")
            lista_comentarios.append(unir_linea(lectura," "))
        i+=1
    
    return lista_fuente,lista_comentarios
def analiza_codigo ():
    """ [Autor : Nicolas]"""
    """[Ayuda : Guardara codigo como lo pide el enunciado] """
    
    # Esta funcion guardará cada archivo ordenado en una lista
    
    lista_archivos = []
    rutas = open("programas.txt", 'r')
    ruta = leer_linea(rutas)
    i = 0
    while ruta: #aaj
        print(ruta)
        i+=1 # Este indice lo creo para distinguir los archivos
        nombre_archivo = (ruta[0]).split("/").pop()
        #Abro ruta dentro de programas.txt
        codigo = open(ruta[0],'r',newline="")
        fuente_unico,comentarios = validar_linea(nombre_archivo,codigo)
        ruta_fuente = "fuente_unico"+str(i) +".csv"
        ruta_comentarios= "comentarios"+str(i) +".csv"
        generar_archivo(fuente_unico,ruta_fuente)
        generar_archivo(comentarios,ruta_comentarios)
        lista_archivos.append(ruta_fuente)
        lista_archivos.append(ruta_comentarios)
        ruta = leer_linea_string(rutas)
    separa_comentarios_fuentes(lista_archivos)
    for archivo in lista_archivos:
        #Elimino los archivos del merge para dejar solo el final
        remove(archivo)
