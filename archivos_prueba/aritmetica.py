#!/usr/bin/env python3

def maximo_comun_divisor(num1, num2):

    if num1>num2:
        resto =  int(num1%num2)
        cociente = int(num1/num2)
        while resto != 0:
            aux = num1
            num1 = num2
            num2 = aux 
            num2 = resto

            cociente = int(num1/resto)
            resto =  int(num1%resto)    
    else:
        num2 = 0 

    return num2

def maximo_comun_multiplo(num1,num2): 
    mcd = maximo_comun_divisor(num1, num2)
    if num1 > num2: 
        mcm = int(num1*num2/mcd)
    else:
        print(' ')
        mcm = 0
    return mcm