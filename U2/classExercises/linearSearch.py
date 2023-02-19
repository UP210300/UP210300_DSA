#Linear search


#Function to find the value in a not sorted list
def linealNotSort(list,value):
    l= 0
    for l in range(len(list)):
        if list[l] == value:
            return l
       
    return -1
           
#Function to find the value in a sorted list
def linealSort(list,value):
    l = 0
    for l in range(len(list)):
        if list[l]== value:
            return l
        elif list[l] > value:
            return -1
        
        

list = [-5,2,3,6,1,9,14]
sortedList = [1,2,3,-5,6,9,12]

input = int( input('Enter the value you desire to look for: '))

#result = linealNotSort(list,input)
result = linealSort(sortedList,input)

if result == -1:
    print ('This value in not in the list')
else:
    print('The value is in the position ', result)