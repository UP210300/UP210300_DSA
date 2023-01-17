#Interaction with the user

import os
import time

print('what is your last name?')
lastName= input()

name= input('what is your name: ')

age = int(input('What is your age: '))

completeName= name + ' ' + lastName
print('Helllo ',completeName,'you are ', age, 'years old :)')
print(type(age))