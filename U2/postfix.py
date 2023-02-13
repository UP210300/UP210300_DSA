
import operator

postfix = '5 6 2 + * 12 4 / -'

p = postfix.split()
p.append(')')

n=0
stack = []

def priority (op):
    if op in ['+','-']:
        return 1
    elif op in ['*','/']:
        return 2
    elif op in ['^']:
        return 3
    elif op in ['()']:
        return 4

ops = { '+' : operator.add, 
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '^' : operator.pow}

while p[n] != ')':
    if p[n] in ['+','-','*','/','^']:
        b=stack.pop()
        a=stack.pop()

        op = p[n]
        priority (op)
        
        if p[n] == '+':
            c= ops['+'](a,b)
        elif p[n] == '-':
            c= ops['-'](a,b)
        elif p[n] == '*':
            c= ops['*'](a,b)
        elif p[n] == '/':
            c= ops['/'](a,b)
        stack.append(c) 
    else:
        operand = int(p[n])
        stack.append(operand)    
    n += 1
value=stack.pop()
print(value)