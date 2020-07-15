def buscar_dato (lista_datos, linea):
    """[Autor : Nicolas]"""
    """[Ayuda : Se le pasa una lista con datos a buscar en la linea del archivo] """

    encontradas = []

    for palabra in lista_datos:
        if palabra in linea:
            encontradas.append(palabra)
    return encontradas

def reemplazar_toda_la_lista (lista,elementos_reemplazados,reemplazo):
    """ [ Autor : Nicolas]"""
    """  [Ayuda : Reemplaza en una lista todos sus elementos]"""

    lista_reemplazada=[]

    for elemento in lista:
        elemento=reemplazar_string(elementos_reemplazados,reemplazo,elemento)
        lista_reemplazada.append(elemento)
    return lista_reemplazada

def ordenamiento_insercion (lista) :

    """ [Autor : Nicolas]"""
    """[ Ayuda : Algoritmo de ordenamiento por insercion visto en clase]"""
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

    """[Autor : Nicolas]"""
    """[Ayuda : Junta las lineas con el metodo join]"""
    return condicion_union.join(linea)

def reemplazar_string (reemplazar,reemplazo,string):
    
    """[ Autor : Nicolas]"""
    """[Ayuda : Con la funcion replace reemplazaremos los datos del parametro reemplazar
        con otro parametro reemplazo]"""
    
    for elemento in reemplazar:
        string=string.replace(elemento,reemplazo)
    return string

