#Bisection method program

def ecuation(x):
    y=(x**2)-2
    return y

a= 1
b= 2
m= (a+b)/2
error= 0.001 #absolut error
e=(b-a)/2 #relative error
i= 1

fa = ecuation(a)
fb = ecuation(b)
fm = ecuation(m)

print('Root fot the function x²-2 \n')

print('-'*65)

print('| i |\t',
    ' a\t|',
    '\tb\t|',
    '\te\t|',
    '\tm\t|',)
print('¯'*65)
print ('|',i,'|',
    '\t{0:.4f}'.format(a),'\t|',
    '\t{0:.4f}'.format(b),'\t|',
    '\t{0:.4f}'.format(e),'\t|',
    '\t{0:.4f}'.format(m),'\t|')



if (fm<0):
    a=m
elif (fm>0):
    b=m

while (e>= error):
    m= (a+b)/2

    fa = ecuation(a)
    fb = ecuation(b)
    fm = ecuation(m)

    if (fm<0):
     a=m
    elif (fm>0):
        b=m
    
    e=(b-a)/2

    i= i+1
    print('-'*65)
    print ('|',i,'|',
    '\t{0:.4f}'.format(a),'\t|',
    '\t{0:.4f}'.format(b),'\t|',
    '\t{0:.4f}'.format(e),'\t|',
    '\t{0:.4f}'.format(m),'\t|')
 

print('-'*65)

print('\nThe root is: ', m)

