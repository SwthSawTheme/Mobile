# -*- coding: utf-8 -*-
def diluir(N):
    cedulas = [100,50,20,10,5,2,1]
    resultado = {}
    
    for cedula in cedulas:
        quantidade = N // cedula 
        resultado[cedula] = quantidade 
        N = N % cedula
    return resultado 

N = int(input(''))
if 0 < N < 1000000:
    resultado = diluir(N)
    for cedula, quantidade in resultado.items():
        print("{} nota(s) de R$ {:.2f}".format(quantidade,float(cedula)).replace(".",","))