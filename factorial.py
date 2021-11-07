# -*- coding: utf-8 -*-
"""

Representar un factorial usando recursividad

"""

def factorial(numero):
    if numero==0:
        return 1
    
    return numero*factorial(numero-1)



if  __name__ ==  '__main__':
    
   print("\t**PROGRAMA OBTENER FACTORIAL USANDO RECURSIVIDAD***\n\n")
   
   numero= input("Introduzca el numero del que desea obtener el factorial: ")
   numero=int(numero)
   print("\n\nEl factorial de {} es: {}".format(numero, factorial(numero)))