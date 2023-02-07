c0 = 16
counter = 0

while (c0 != 1):
    if (c0 % 2 == 0) :
     c0 /= 2
    else:
        c0 = 3* c0 +1
    print(c0)
    counter += 1

print('steps = ', counter)
