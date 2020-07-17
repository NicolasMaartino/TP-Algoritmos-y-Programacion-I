#!/usr/bin/env python3
def imprimir(dicc_desarrolladores,total_lineas):
    total_desarrollador = 0
    with open("participacion.txt","w") as informe:
        total_funciones = 0
        linea = '-'*50
        print('\n\tInforme de Desarrollo por Autor\n')
        print(linea)
        informe.write('\n\tInforme de Desarrollo por Autor\n'+'\n')
        informe.write(linea)

        for autor,funciones in dicc_desarrolladores.items():
            acum_lineas = 0
            cant_funciones_desarrollador = 0
            print('\nAutor:  {}\n'.format(autor))
            informe.write('\nAutor:  {}\n'.format(autor))
            print('\tFunción\t\tLineas')
            informe.write('\tFunción\t\tLineas'+'\n')
            informe.write(linea+'\n')
            lista_funciones = sorted(funciones, key= lambda funcion:funcion[1])
            total_funciones += len(lista_funciones)
            for data in lista_funciones:
                cant_funciones_desarrollador += 1
                acum_lineas += data[1]
                print("\t{}\t{}".format(data[0],data[1]))
                informe.write("{}\t\t{}".format(data[0],data[1])+'\n')
                porcentaje=(acum_lineas*100)//total_lineas
            print("\t{} Funciones-lineas\t{}\t{}%".format(cant_funciones_desarrollador,acum_lineas,porcentaje))
            informe.write("\t{}Funciones-Lineas\t{}\t{}%".format(cant_funciones_desarrollador,acum_lineas,porcentaje))
        print('\nTotal Funciones {} - Lineas {}'.format(total_funciones,total_lineas))
        informe.write('\n\nTotal Funciones {} - Lineas {}'.format(total_funciones,total_lineas)+'\n')
