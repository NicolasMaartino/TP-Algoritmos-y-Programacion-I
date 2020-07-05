#!/usr/bin/env python3
#Hacer un programa que importe un modulo blablablablabla
#blablablablabla
#balablabal
#balabala

import aritmetica

def main():
    
    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese otro numero: '))
    resultado_mcd = aritmetica.maximo_comun_divisor(num1,num2)
    resultado_mcm = aritmetica.maximo_comun_multiplo(num1, num2)
    if resultado_mcd != 0:
        print('El MCD de {} y {} es: {} '.format(num1,num2,resultado_mcd))
        print('EL MCM de {} y {} es: {}'.format(num1,num2, resultado_mcm))
    else:
        print('Ingreso Incorrecto')

main()