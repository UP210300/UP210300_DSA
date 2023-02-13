
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