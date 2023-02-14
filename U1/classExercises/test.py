
import numpy as np

A = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#A = [[C * i + j + 1 for j in range(C)] for i in range(F)]  # 4 X 3
A = np.array(A)
print(A)

#matriz de numeros sin repetir
#dimensión nxn
#aleatorio

import random
import numpy as np

m = int(input('Please enter the dimensions of the matrix that you desire: '))
n = m

matrix = np.empty((m,n), dtype=int, order='C')
           
for i in range(m):
    for j in range(n):
        m = 0
        n = 0
        matrix [m][n] == int(random.randint(0, 100))
        n += 1
        n += 1
            
print (matrix) 

from random import randint

def fillArray(n):
    array = []

    for row in range(n):
        row2 = []

        for col in range(n):
            row2.append(randint(1,1000))

        array.append(row2)
    
    return array

result = fillArray(5)

print(result)

import random
L=[random.randint(80, 99)] #este es L[0]
i=1
while i<10:
  x=random.randint(80,99)
  for j in range(0, len(L)):
    if L[j]==x:
      break
  else:
    L.append(x)
    i+=1
print(L)
print(sorted(L))

#matriz de numeros sin repetir
#dimensión nxn
#aleatorio

import numpy as np
from random import randint
import random

def fillArray(n):
    array = []

    for r in range(n):
        row = []
        i = 0
        while i > n:
            x=random.randint(1,100)
            for j in range(0, len(row)):
                if row[j]==x:
                    break
            else:
                row.append(x)
                i+=1
        #for c in range(n):
          # row.append(randint(1,1000))

        array.append(row)
    
    return array

d = int(input('Please enter the dimensions of the matrix that you desire: '))
matrix = np.array(fillArray(d))

print(matrix)

import random


def crear_matriz(n):
    matriz = []
    filas = n
    columnas = n
    for f in range(filas):
        matriz.append([0]*columnas)
    return matriz

def rellenar(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(0, orden**2)
            
            
    return matriz


def imprimir(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range (columnas):
            print("%3d" %matriz[f][c], end= "")
        print()


orden = int(input("Ingrese el orden de la matriz: "))

matriz = crear_matriz(orden)

rellenar(matriz)

imprimir(matriz)