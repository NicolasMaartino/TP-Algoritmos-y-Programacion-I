dic = {'buscar_dato': {'Parametros': 'lista_datos ', 'Lineas': 6, 'Invocaciones': 0, 'Returns': 0, 'If/elif': 0, 'for': 0, 'while': 0, 'Break': 0, 'Exit': 0, 'Coment': 0, 'Ayuda': '', 'Autor': 'Nicolas'},
       'ordenamiento_insercion': {'Parametros': 'lista', 'Lineas': 13, 'Invocaciones': 0, 'Returns': 0, 'If/elif': 0, 'for': 0, 'while': 0, 'Break': 0, 'Exit': 0, 'Coment': 0, 'Ayuda': '', 'Autor': 'Nicolas'},
       'reemplazar_string': {'Parametros': 'reemplazar reemplazo string):', 'Lineas': 5, 'Invocaciones': 0, 'Returns': 0, 'If/elif': 0, 'for': 0, 'while': 0, 'Break': 0, 'Exit': 0, 'Coment': 0, 'Ayuda': '', 'Autor': 'Nicolas'},
       'reemplazar_toda_la_lista': {'Parametros': 'lista elementos_reemplazados reemplazo):', 'Lineas': 6, 'Invocaciones': 0, 'Returns': 0, 'If/elif': 0, 'for': 0, 'while': 0, 'Break': 0, 'Exit': 0, 'Coment': 0, 'Ayuda': '', 'Autor': 'Nicolas'},
       'unir_linea': {'Parametros': 'linea condicion_union', 'Lineas': 2, 'Invocaciones': 0, 'Returns': 0, 'If/elif': 0, 'for': 0, 'while': 0, 'Break': 0, 'Exit': 0, 'Coment': 0, 'Ayuda': 'Si', 'Autor': 'Nicolas'}}

def imprimir(dic):
    """[Autor: Lucia]"""
    """[Ayuda: Crea la una tabla]"""
    Tabla = """\
+-----------------------------------------------------------------------------------------------------------------------------------------------+
|        FUNCION                Parametros   Líneas   Invocaciones   Returns   If/elif    for   while   Break   Exit   Coment  Ayuda    Autor   |
------------------------------------------------------------------------------------------------------------------------------------------------|
{}
+-----------------------------------------------------------------------------------------------------------------------------------------------+\
"""
    Tabla = (Tabla.format('\n'.join('|{0:24}\t{1:5}\t{2:8}\t{3:5}\t{4:9}\t{5:4}\t{6:4}\t{7:3}\t{8:3}\t{9:3}\t{10:3}\t{11:1}\t{12:8}|'.format(funcion, dic[funcion]["Parametros"].count(" "), dic[funcion]["Lineas"], dic[funcion]["Invocaciones"], dic[funcion]["Returns"],
                                                                                 dic[funcion]["If/elif"], dic[funcion]["for"], dic[funcion]["while"], dic[funcion]["Break"], dic[funcion]["Exit"], dic[funcion]["Coment"],
                                                                                                                      dic[funcion]["Ayuda"], dic[funcion]["Autor"])
     for funcion in dic)))
    print (Tabla)

imprimir(dic)
    
        
