# -*- coding: utf-8 -*-
"""

Programa para fundamentos de python

FUTURE DEVELOPERS

Aaron Merlos

"""

# Este es un comentario de linea para cometar codigo

'''
Este es un comentario multilinea para poner notas
'''

var1 = 3 
var2 = 2.0
var3 ,var4 = False, True 
#var3 ,var4 = 0, 1 es equivalente a la forma booleana
var5 = '3.4'
var6 = [] #list()
var7 = {} #dict()
var7_2 = () #tuple()

'''
USO EN CONSOLA


OPERADORES
True == False
True < False
True > False
True <= False
True >= False
True is False
True is not False
lista = [1,2,3,4,5]
3 in lista #True
8 in lista #False



LISTAS
Lista = [1, False, 3.4, 'cadena'] #La lista en python admite diferentes tipos de valores
lista[2] = 5.5 #sustituye el valor correspondiente en n-1
lista.append('elemento nuevo') #Agrega el elemento al final de la lista
dir(lista) #muestra todos los comandos que se pueden utilizar para listas
lista = [3,6,3,6,9,7,4,2]
lista.sort() #ordena de menor a mayor los elementos de la lista

TUPLAS
tupla = (2,3,4,) #coma al final para que se identifique como tupla
tupla[2] = 3 #ERROR, son inmutables las tuplas
listaNew = list(tupla)
type(listaNew) #la tupla se convierte en lista y ahora si se pueden cambiar valores

STRINGS
var = 'variable 1'
var = variable multilinea'
var[-1] #nos da el ultimo caracter de la cadena
var[::-1] #nos devuelve la cadena invertida (funciona tambien con listas)
nomenclatura var[desde(num posicion):hasta(num posicion):sentido(+-1)]
len(var) #longitud de una cadena

for car in range(0,len(var)):
    print(var[car])
    
for car in range(len(var)-1, 0, -1):
    print(var[car])
    
#Para insertar un  caracter o un conjunto de caracteres en una seccion determinada de una cadena
cadena2 = var[0:3] + 'f' + var[4:]

numero=4
'el numero vale: {}'.format(numero)

DICCIONARIOS
diccionarios = dict()
diccionario = {}

dicci = {'nombre':'roberto','edad':28}
dicci['nombre']
dicci['edad']
dicci.keys() #consultar llaves del diccionario

for i in dicci.values():
    print(i)
    
for i in dicci.keys():
    print(i)
    
for i,j in dicci.items():
    print(f'llave: {i} \t valor: {j}')
    
del dicci['edad'] #eliminar del diccionario
del dicci #eliminar todo el diccionaio




'''
#%%

#CICLOS


dicci = {'nombre':'roberto','edad':28}

if dicci["edad"] > 35:
    print('viejo')
elif dicci["edad"] > 25 and dicci["edad"] <= 35:
    print('chavo ruco')
else:
    print('no tan viejo')

#Forma alternativa de if

variable = 'jovenazo' if dicci['edad'] < 35 else 'viejito'
print(variable)


var = 5
while (var<10):
    print(var)
    var += 1

var = 5
while(True): #while infinito
    print(var)
    var += 1
    if var > 10:
        break

#%%

#FUNCIONES

def suma(num1, num2):
    global z
    return num1 + num2 + z

z=3
x=4
y=5
print(suma(x,y))

def returnlist():
    for num in range(0,1000000):
        yield num    #para optimizar espacio de memoria


#%%

#POO

class Person:
    
    nombre = ''
    edad = 0
    estatura = 0
    posicion = 0
    
    def __init__(self, nombre, edad, estatura):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        
    def caminaAdelante(self, pasos):
        self.posicion += pasos
        print(f'{self.nombre} esta en: {self.posicion}')
        
    def caminaAtras(self, pasos):
        self.posicion -= pasos
        print(f'{self.nombre} regreso: {self.posicion}')
        
class Job(Person):
    
    trabajo = ''
    inicio = ''

    def __init__(self, nombre, edad, estatura, trabajo, inicio):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.trabajo = trabajo
        self.inicio = inicio
        
'''
EN CONSOLA

from script import Job
Juan = Job('Juan Perez', 45, 1.78, 'ingeniero', '02-07-2020')
Juan.nombre

'''






#%%