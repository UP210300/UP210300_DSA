#matrix of random numbers

import numpy as np
from random import randint

#function to fill matrix
def fillArray(n):
    array = []

    for r in range(n):
        row = []
    
        for c in range(n):
           row.append(randint(1,1000))#generate random numbers

        array.append(row)
    
    return array

#print matrix
d = int(input('Please enter the dimensions of the matrix that you desire: '))
matrix = np.array(fillArray(d))

print(matrix)