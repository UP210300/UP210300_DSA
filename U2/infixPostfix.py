q = '5 * ( 6 + 2 ) - 12 / 4'
q = q.split()
q.insert(0,'(')
q.append(')')


p = [] #postfix expresion
stack = [] #operators
n = 0
s = 0


def priority (op):
    if op in ['+','-']:
        return 1
    elif op in ['*','/']:
        return 2
    elif op in ['^']:
        return 3
    elif op in ['(',')']:
        return 0

while n < len(q):
    if q[n] == '(': #add '(' to operator stack
        stack.append(q[n])
    elif q[n] == ')': #remove from stack each operator and add it to posrfix array until '(' is encountared
        s = (len(stack)-1)
        while stack != [] and stack[s] != '(':
            op = stack.pop()
            p.append(op)
            s -= 1
        stack.pop()
    elif q[n] in ['+','-','*','/','^']: #operand encountered
        prior = priority(q[n])
        precedence = priority(stack[len(stack)-1])
        while stack != [] and  precedence  >=  prior:
            op = stack.pop()  
            p.append(op)
            precedence = priority(stack[len(stack)-1])
        stack.append(q[n])
    else: #add opperand to postfix array
        p.append(q[n])
    n += 1
print(p)