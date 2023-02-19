#binary search

#function 
def binarySearch(list,value):

    ll = 0
    ul = len(list)-1
    md = (ll+ul)//2
    c = 0

    if value == list[md]:
        position = md
        c = 1
    else:
        while ll <= ul and value != list[md]:
            if value < list[md]:
                ul = md - 1
            elif value > list[md]:
                ll = md + 1
            md = (ll+ul)//2
            c += 1
        if list[md] == value:
            position = md
        else:
            position = False
        
    return position,c
            
        
list = [-3,0,1,5,7,9]
value = 4
x,y = binarySearch(list,value)
if x == False:
    print('The number you are lookig for is not in this list')
else:
    print('The number',value, 'is in the position',x,'\nThe number of iterations was: ',y)


