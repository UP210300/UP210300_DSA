#postfix to value

import operator

p=[5,6,2,'+','*',12,4,'/','-']
p.append(')')

n = 0
stack = []

ops = { '+' : operator.add, 
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '^' : operator.pow}

while p[n] != ')':
    if type(p[n]) == int:
        stack.append(p[n])
    else:
        b=stack.pop()
        a=stack.pop()
        if p[n] == '+':
            c= ops['+'](a,b)
        elif p[n] == '-':
            c= ops['-'](a,b)
        elif p[n] == '*':
            c= ops['*'](a,b)
        elif p[n] == '/':
            c= ops['/'](a,b)
        stack.append(c)  
    n += 1
value=stack.pop()
print(value)




