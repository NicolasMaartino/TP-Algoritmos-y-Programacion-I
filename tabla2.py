#!/usr/bin/env python3
def imprimir(dicc_desarrolladores,total_lineas):
    with open("participacion.txt","w") as informe:
        total_funciones = 0
        linea = '-'*50
        print('\n\tInforme de Desarrollo por Autor\n')
        informe.write('\n\tInforme de Desarrollo por Autor\n'+'\n')
        for autor,funciones in dicc_desarrolladores.items():
            print('\nAutor:  {}\n'.format(autor))
            informe.write('\nAutor:  {}\n'.format(autor))
            print('Función\t\tLineas')
            informe.write('Función\t\tLineas'+'\n')
            print(linea)
            informe.write(linea+'\n')
            lista_funciones = sorted(funciones, key= lambda funcion:funcion[1])
            total_funciones += len(lista_funciones)
            for data in lista_funciones:
                print("{}\t{}".format(data[0],data[1]))
                informe.write("{}\t\t{}".format(data[0],data[1])+'\n')
        print('Total Funciones {} - Lineas {}'.format(total_funciones,total_lineas))
        informe.write('Total Funciones {} - Lineas {}'.format(total_funciones,total_lineas)+'\n')
