#!/usr/bin/env python3
def leer_archivos_csv (archivocsv):
    """Autor : Alejandro"""
    """Ayuda : leer archivos .csv y devuelve una lista de ellos para un mejor estudio"""
    linea = archivocsv.readline()
    return linea.rstrip('\n').split(',') if linea else ""
def grabar_nuevo (archivo,linea):
    """Autor : Alejandro"""
    """Ayuda : genera un archivo unificado, es decir archivo2.csv+archivo1.csv"""
    archivo.write(",".join(linea) +'\n')
def tipo_archivos (archivo1):
    """Autor : Alejandro"""
    """Ayuda : valida si el archivo recibido es comentarios o fuente_unico"""
    if "comentarios" in archivo1:
        archivo3 = "comentarios_unificado.csv"
    else:
        archivo3 = "fuente_unificado.csv"
    return archivo3
def merge (archivo1,archivo2):
    """Autor : Alejandro"""
    """Ayuda : unifica archivo1.csv y archivo2.csv en un solo archivo"""
    archivo3 = tipo_archivos(archivo1)
    with open(archivo1,"r") as archivo1, open(archivo2,"r") as archivo2,\
        open(archivo3,"w") as archivo_mezcla:
            linea_archivo1 = leer_archivos_csv(archivo1)
            linea_archivo2 = leer_archivos_csv(archivo2)
            while linea_archivo1 and linea_archivo2:
                if linea_archivo1[0] ==  linea_archivo2[0]:
                    grabar_nuevo(archivo_mezcla,linea_archivo2)
                    grabar_nuevo(archivo_mezcla,linea_archivo1)
                    linea_archivo1 = leer_archivos_csv(archivo1)
                    linea_archivo2 = leer_archivos_csv(archivo2)
                elif linea_archivo1[0] < linea_archivo2[0]:
                    grabar_nuevo(archivo_mezcla,linea_archivo1)
                    linea_archivo1 =leer_archivos_csv(archivo1)
                else:
                    grabar_nuevo(archivo_mezcla,linea_archivo2)
                    linea_archivo2 = leer_archivos_csv(archivo2)
    return archivo3
