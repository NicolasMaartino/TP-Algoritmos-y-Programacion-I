def reemplazar_string (reemplazar,reemplazo,string):
    """[ Autor : Nicolas]"""
    """ [Ayuda : Con la funcion replace reemplazaremos los datos del parametro reemplazar
        con otro parametro reemplazo]"""
    for elemento in reemplazar:
        string=string.replace(elemento,reemplazo)
    return string

def leer_linea_string (archivo) :
    """[ Autor : Nicolas]"""
    """[Ayuda : lee una linea de un archivo y devuelve un string]"""
    return archivo.readline().strip() 

def leer_linea (archivo) :
    """[Ayuda : lee una linea del archivo y devuelve una lista]"""
    # Esta a diferencia de la otra leer_linea ya corta por espacio con el split()
    linea = archivo.readline().strip().split()
    if linea:
        devolver = linea
    else:
        devolver = "","",""
    """ [Autor : Nicolas]"""
    return devolver

def analiza_codigo () :
    """[ Autor : Nicolas]"""
    """[Ayuda : Guardara codigo como lo pide el enunciado]"""
    # Esta funcion guardará cada archivo ordenado en una lista
    lista_archivos = []
    with open("programas.txt", 'r') as rutas:
        ruta = leer_linea_string(rutas)
        i = 0
        while ruta: # aaj
            i+=1 # Este indice lo creo para distinguir los archivos
            nombre_archivo = ruta.split("/").pop()
            with open(ruta,'r') as codigo:
                fuente_unico,comentarios = validar_linea(nombre_archivo,codigo)
                ruta_fuente = "fuente_unico"+str(i) +".csv"
                ruta_comentarios= "comentarios"+str(i) +".csv"
                generar_archivo(fuente_unico,ruta_fuente)
                generar_archivo(comentarios,ruta_comentarios)
                lista_archivos.append(ruta_fuente)
                lista_archivos.append(ruta_comentarios)
            ruta = leer_linea_string(rutas)
    return lista_archivos

def grabar_archivo (archivo,leyenda) :
    """[Autor : Nicolas]"""
    """[Ayuda : Graba linea en un archivo pasado por parametro] """
    archivo.write(leyenda)

def generar_archivo (lista,ruta) :
    """[Autor : Nicolas]"""
    """[Ayuda : Genera un archivo a traves de un iterable]"""
    archivo = open(ruta,"w")
    for funcion in lista:
        leyenda = ",".join(funcion)+"\n"
        grabar_archivo(archivo,leyenda)
    archivo.close()

def ordenamiento_insercion (lista) :
    """[Autor : Nicolas]"""
    """[Ayuda : Algoritmo de ordenamiento por insercion visto en clase]"""
    for indice in range(1,len(lista)):
        valor = lista[indice]
        i = indice-1
        variable = True
        while i >= 0 and variable == True:
            if valor<lista[i]:
                lista[i+1] = lista[i]
                lista[i] = valor
                i = i-1
            else:
                variable = False
    return lista

def validar_linea (nombre_modulo,archivo) :
    """[Autor : Nicolas]"""
    """[Ayuda : Va a validar las lineas del archivo para saber 
        a cual de las dos salidas (comentarios y fuente unico) va a ir]"""
    funciones_fuente = [] # Aca iran a parar las funciones para fuente codigo 
    funciones_comentarios = [] # Y aca las funciones para comentarios
    lectura = leer_linea(archivo)
    while lectura[0]:
        if lectura[0] == "def":
            nombre_funcion = lectura[1] # Es el nombre de la funcion porque es la linea de def
            parametros = lectura[2].replace(","," ") # Y aca los parametros 
            linea_fuente = [nombre_funcion,parametros,nombre_modulo]
            linea_comentarios = [nombre_funcion] 
            lectura = leer_linea(archivo)
            while lectura[0] != "def" and lectura[0] != "":
                lectura[0]=reemplazar_string(['"""'],"",lectura[0])
                if "[Ayuda" in lectura or "Ayuda" in lectura :
                    union = unir_linea(lectura," ")
                    union = reemplazar_string(['"""','[',"]","Ayuda",":"],"",union).strip()
                    linea_comentarios.insert(2,union)
                elif "[Autor" in lectura or "Autor" in lectura :
                    union = unir_linea(lectura," ")
                    union = reemplazar_string(['"""','[',']',"Autor",":"],"",union).strip()
                    linea_comentarios.insert(1,union)
                    linea_fuente.insert(3,union)
                else:
                    if "#" not in lectura :
                        linea_fuente.append(unir_linea(lectura,","))
                    else:
                        linea_fuente,linea_comentarios = seccion_comentarios(lectura,linea_comentarios,linea_fuente)
                lectura = leer_linea(archivo)
            funciones_fuente.append(linea_fuente)
            funciones_comentarios.append(linea_comentarios)
        lectura = leer_linea(archivo)
    return ordenamiento_insercion(funciones_fuente),ordenamiento_insercion(funciones_comentarios)

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
            lista_fuente.append(unir_linea(fuente_unico,","))
            lista_comentarios.append(unir_linea(comentario,","))
        elif elemento == "#" and i==0 :
            encontro = True
            lista_comentarios.append(unir_linea(lectura,","))
        i+=1
    return lista_fuente,lista_comentarios

def unir_linea (linea,condicion_union) :
    """[Autor : Nicolas]"""
    """[Ayuda : Junta las lineas con el metodo join]"""
    return condicion_union.join(linea).replace(","," ")


analiza_codigo()




