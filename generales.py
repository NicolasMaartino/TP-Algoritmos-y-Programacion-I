from archivos import leer_linea
def listar_archivo (archivo):
    """ [Autor : Lucia] """
    """ [Ayuda : convierte al archivo en una lista donde cada elemento es una linea del mismo] """
    lista_ar = []
    linea = (leer_linea(archivo,","))
    while linea:
        lista_ar.append(linea.split(","))
        linea = leer_linea(archivo,",")
    return lista_ar

def agregar_linea_especifica(indice,linea,lista):
    """ [Autor : Nicolas]
       [Ayuda : Agrega una linea especifica a una lista]
    """
    union = unir_linea(linea," ").strip()
    lista.insert(indice,union)
    return lista

def item_necesario(linea,eliminar,condicion):
    """[Autor : Nicolas]
       [Ayuda : Esta funcion va a buscar un dato exacto y hara lo que necesites con el.
          Convertira todo a un nuevo strin y una nueva lista que con el metodo extend
          se unira a la lista final]
    """
    i=0
    nueva_lista=[]
    for elementos in linea:
        nuevo_string=""
        for letras in elementos:
            if eliminar == letras:
                nuevo_string+=condicion
            else:
                nuevo_string+=letras
        lista=nuevo_string.split()
        nueva_lista.extend(lista)
        i+=1
    return nueva_lista

def tipo_archivos (archivo):
    """ Autor : Alejandro """
    """ Ayuda : valida si el archivo recibido es comentarios o fuente_unico """
    if "comentarios" in archivo:
        archivo_unico = "comentarios.csv"
    else:
        archivo_unico = "fuente_unico.csv"
    return archivo_unico

def buscar_dato (lista_datos,linea):
    """ [Autor : Nicolas] """
    """ [Ayuda : Se le pasa una lista con datos a buscar en la linea del archivo] """

    encontradas = []

    for palabra in lista_datos:
        if palabra in linea:
            encontradas.append(palabra)
    return encontradas

def reemplazar_toda_la_lista (lista,elementos_reemplazados,reemplazo):
    """ [ Autor : Nicolas] """
    """  [Ayuda : Reemplaza en una lista todos sus elementos] """

    lista_reemplazada=[]

    for elemento in lista:
        elemento=reemplazar_string(elementos_reemplazados,reemplazo,elemento)
        lista_reemplazada.append(elemento)
    return lista_reemplazada

def ordenamiento_insercion (lista) :

    """ [Autor : Nicolas] """
    """ [ Ayuda : Algoritmo de ordenamiento por insercion visto en clase] """
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

def unir_linea (linea,condicion_union) :

    """ [Autor : Nicolas] """
    """ [Ayuda : Junta las lineas con el metodo join] """
    return condicion_union.join(linea)

def reemplazar_string (reemplazar,reemplazo,string):
    
    """ [ Autor : Nicolas] """
    """ [Ayuda : Con la funcion replace reemplazaremos los datos del parametro reemplazar
        con otro parametro reemplazo] """
    
    for elemento in reemplazar:
        string=string.replace(elemento,reemplazo)
    return string

def validacion_archivo_programas ():

    """ [ Autor : Alejandro] """
    """ [Ayuda : Preguntaremos si hay alguna ruta en programas.txt] """

    archivo = open("programas.txt")
    linea = archivo.readline()
    validacion = False
    if not linea:
        validacion = True
    archivo.seek(0)
    archivo.close()
    return validacion













