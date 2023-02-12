#Bisection method program

#function for the ecuation x²-2
def ecuation(x):
    y=(x**2)-2
    return y

#interval of the function
a = 1
b = 2

#calculate midpoint
m = (a+b)/2

#absolut error
error = 0.001 

#calculate relative error
e =(b-a)/2 

#number of iterations
i = 1

#evaluate function 
fa = ecuation(a)
fb = ecuation(b)
fm = ecuation(m)

#header
print('Root of the function x²-2 \n')

print('-'*65)

print('| i |\t',
    ' a\t|',
    '\tb\t|',
    '\te\t|',
    '\tm\t|',)
print('¯'*65)

#value of the first iteration
print ('|',i,'|',
    '\t{0:.4f}'.format(a),'\t|',
    '\t{0:.4f}'.format(b),'\t|',
    '\t{0:.4f}'.format(e),'\t|',
    '\t{0:.4f}'.format(m),'\t|')


#determine the new interval
if (fm<0):
    a=m
elif (fm>0):
    b=m

#iteration while relative error(e) is greater than absolute error(error)
while (e>= error):
    #calculate midpoint
    m= (a+b)/2

    #evaluate function acording to the new interval
    fa = ecuation(a)
    fb = ecuation(b)
    fm = ecuation(m)

    #determine the new interval
    if (fm<0):
        a=m
    elif (fm>0):
        b=m
    
    #calculate relative error
    e=(b-a)/2

    #count iterations
    i= i+1

    #fill table
    print('-'*65)
    print ('|',i,'|',
    '\t{0:.4f}'.format(a),'\t|',
    '\t{0:.4f}'.format(b),'\t|',
    '\t{0:.4f}'.format(e),'\t|',
    '\t{0:.4f}'.format(m),'\t|')
 
print('-'*65)

print('\nThe root is: ', m)

