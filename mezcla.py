#!/usr/bin/env python3
def leer_archivos_csv (archivocsv):
    """Autor : Alejandro"""
    """Ayuda : leer archivos .csv y devuelve una lista de ellos para un mejor estudio"""
    linea = archivocsv.readline()
    return linea.rstrip('\n').split(',') if linea else ""
def grabar_nuevo (archivo,linea):
    """Autor : Alejandro"""
    """Ayuda : genera un archivo unificado, es decir fuente_unicox.csv+comentariosx.csv"""
    archivo.write(",".join(linea) +'\n')
def merge (archivo1,archivo2):
    """Autor : Alejandro"""
    """Ayuda : unifica comentariosx.csv y fuente_unicox.csv en un solo archivo"""
    archivo3 = "archivo_unificado.csv"
    with open(archivo1,"r") as comentariosx, open(archivo2,"r") as fuente_unicox,\
        open(archivo3,"w") as archivo_mezcla:
            linea_comentarios = leer_archivos_csv(comentariosx)
            linea_fuente = leer_archivos_csv(fuente_unicox)
            while linea_comentarios and linea_fuente:
                if linea_comentarios[0] ==  linea_fuente[0]:
                    grabar_nuevo(archivo_mezcla,linea_fuente)
                    grabar_nuevo(archivo_mezcla,linea_comentarios)
                    linea_comentarios = leer_archivos_csv(comentariosx)
                    linea_fuente = leer_archivos_csv(fuente_unicox)
                elif linea_comentarios[0] < linea_fuente[0]:
                    grabar_nuevo(archivo_mezcla,linea_comentarios)
                    linea_comentarios =leer_archivos_csv(comentariosx)
                else:
                    grabar_nuevo(archivo_mezcla,linea_fuente)
    return archivo3