from random import randrange


for i in range(5):
   n= randrange(1,11)
   a = n
   while a == n:
      n= randrange(1,11) 
   print(n)
   
