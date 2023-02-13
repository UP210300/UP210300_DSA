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