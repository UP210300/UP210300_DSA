import operator

expression = input('Enter a expression: ') # 5*(6+2)-12/4
infix = expression.split()
infix.insert(0,'(')
infix.append(')')

ops = { '+' : operator.add, 
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '^' : operator.pow}

def priority (op):
    if op in ['+','-']:
        return 1
    elif op in ['*','/']:
        return 2
    elif op in ['^']:
        return 3
    elif op in ['(',')']:
        return 0

def infixToPostfix (infix):
    postfix = [] #postfix expresion
    stack = [] #operators
    n = 0
    s = 0
    while n < len(infix):
        if infix[n] == '(':  # add '(' to operator stack
            stack.append(infix[n])
        # remove from stack each operator and add it to posrfix array until '(' is encountared
        elif infix[n] == ')':
            s = (len(stack)-1)
            while stack != [] and stack[s] != '(':
                op = stack.pop()
                postfix.append(op)
                s -= 1
            stack.pop()
        elif infix[n] in ['+', '-', '*', '/', '^']:  # operand encountered
            prior = priority(infix[n])
            precedence = priority(stack[len(stack)-1])
            while stack != [] and precedence >= prior:
                op = stack.pop()
                postfix.append(op)
                precedence = priority(stack[len(stack)-1])
            stack.append(infix[n])
        else:  # add opperand to postfix array
            postfix.append(infix[n])
        n += 1
    return postfix

def postfixToValue(postfix):
    postfix.append(')')
    n=0
    stack = []
    while postfix[n] != ')':
        if postfix[n] in ['+','-','*','/','^']:
            
            b=stack.pop()
            a=stack.pop()
            
            if postfix[n] == '+':
                c= ops['+'](a,b)
            elif postfix[n] == '-':
                c= ops['-'](a,b)
            elif postfix[n] == '*':
                c= ops['*'](a,b)
            elif postfix[n] == '/':
                c= ops['/'](a,b)
            elif postfix[n] == '^':
                c= ops['^'](a,b)
            stack.append(c) 
        else:
            operand = int(postfix[n])
            stack.append(operand)    
        n += 1
    value = stack.pop()
    return value

postfix = infixToPostfix(infix)
result = postfixToValue(postfix)

print(result)