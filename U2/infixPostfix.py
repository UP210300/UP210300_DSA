q = '( 5 * ( 6 + 2 ) - 1 2 / 4 )'
q = q.split()
q.insert(0,'(')
q.append(')')
print(q)
p = []
stack = []
n = 0
