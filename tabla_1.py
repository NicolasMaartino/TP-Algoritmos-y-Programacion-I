def tabla(archivo):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Funcion que acumula nombres de funciones para luego dibujarlas en una tabla]"""
    contador=0
    nueva_lista=[]
    linea=leer_archivo(archivo)
    print("{}".format("Funciones:"))
    while linea!=[""] or nueva_lista!=[""]:
        if contador!=5:
            nueva_lista.append(linea[0])
            contador+=1
        else:
            print("\n{0}  {1}  {2}  {3}  {4}".format(nueva_lista[0], nueva_lista[1], nueva_lista[2], nueva_lista[3], nueva_lista[4]))
            nueva_lista=[]
            contador=0
            nueva_lista.append(linea[0])
        linea=leer_archivo(archivo)
    return


funciones=open("comentarios.txt", "r")
tabla(funciones)
funciones.close()

