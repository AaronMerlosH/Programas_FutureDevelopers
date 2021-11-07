# -*- coding: utf-8 -*-
"""

Dado un arreglo que contiene una serie de numerosdefine el primer digito que se repita en 
dicho arreglo, ejemplo:
    
Para:
a = [2, 1, 3, 5, 3, 2]
        
La salida debe ser:
firstDuplicate(a) = 3
        

FUTURE DEVELOPERS

Aaron Merlos

"""

def firstDuplicate(a):
    
    dict = {}
    result = -1
    
    for i in range(0 , len(a)):
        
        element = a[i]
        if element not in dict.keys():
            dict[element] = True
        else:
            result = element
            break
            
    return result

result1 = firstDuplicate([2, 1, 3, 5, 3, 2])

try: 
    result1 = str(result1)
except Exception as error:
    print("excepcion es: {} : {}".format(type(error),error))
    print("No se puede convertir el numero {}".format(result1))
    
print('\n\nEl primer valor duplicado detectado es: ' + result1)



