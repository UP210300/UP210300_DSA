'''

import mypkg.sibling         //librebia.metodo
from mypkg import sibling

'''

#Hash

print(int('5')+5) # int to change a string to integer

keywords = ['False','None','True','and']

print(keywords[1], len(keywords)) #len gives the lenght of the array

#Function

def double (x):
    y= x*2
    return y

print(double(2))

a = [5,2,7,9,3]

for i in range (0, len(a)):
    print(a[1])

#Bubble sort
for i in range(0,len(a)+1 -2):
    for j in range(0,len(a)+1 -i-2):
        x = a[j]
        y= a[j+1]
        if x >y:
            a[j] = y
            a[j+1] = x

print(a)

#Conditional

b=10
if b>10:
    print(':P')
else:
    print(':)')

