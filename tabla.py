dic = {'generar_archivo': {'Nombre': 'generar_archivo.TP grupal\\TP1-nicolas\\archivos.py', 'Parametros': 'lista ruta',
                           'Lineas': 6, 'Invocaciones': 0, 'return': 0, 'If/elif': 0, 'for': 0, 'while': 0, 'Break': 0, 'Exit': 0,
                           'Coment': 0, 'Ayuda': '', 'Autor': ''}, 'grabar_archivo': {'Nombre': 'grabar_archivo.archivos.py',
                                                                                      'Parametros': 'archivo leyenda', 'Lineas': 2, 'Invocaciones': 0, 'return': 0, 'If/elif': 0, 'for': 0, 'while': 0, 'Break': 0, 'Exit': 0, 'Coment': 0, 'Ayuda': '', 'Autor': ''}, 'leer_linea': {'Nombre': 'leer_linea.C:\\Users\\lucialiceri\\OneDrive - fi.uba.ar\\FIUBA\\ALGO I - Guarna\\TP grupal\\TP1-nicolas\\archivos.py', 'Parametros': 'archivo', 'Lineas': 7, 'Invocaciones': 0, 'return': 0, 'If/elif': 0, 'for': 0, 'while': 0, 'Break': 0, 'Exit': 0, 'Coment': 0, 'Ayuda': '', 'Autor': ''}, 'leer_linea_string': {'Nombre': 'leer_linea_string.C:\\Users\\lucialiceri\\OneDrive - fi.uba.ar\\FIUBA\\ALGO I - Guarna\\TP grupal\\TP1-nicolas\\archivos.py', 'Parametros': 'archivo', 'Lineas': 2, 'Invocaciones': 0, 'return': 0, 'If/elif': 0, 'for': 0, 'while': 0, 'Break': 0, 'Exit': 0, 'Coment': 0, 'Ayuda': '', 'Autor': ''}}
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
    Tabla = (Tabla.format('\n'.join('|{0:30}\t{1:5}\t{2:8}\t{3:5}\t{4:9}\t{5:4}\t{6:4}\t{7:3}\t{8:3}\t{9:3}\t{10:3}\t{11:1}\t{12:8}|'.format(dic[funcion]["Nombre"], dic[funcion]["Parametros"].count(" "), dic[funcion]["Lineas"],
                                            dic[funcion]["Invocaciones"], dic[funcion]["return"],
                                                                                 dic[funcion]["If/elif"], dic[funcion]["for"], dic[funcion]["while"], dic[funcion]["break"], dic[funcion]["exit"], dic[funcion]["Coment"],
                                                                                                                      dic[funcion]["Ayuda"], dic[funcion]["Autor"])
     for funcion in dic)))
    print (Tabla)

#imprimir(dic)
    
        
