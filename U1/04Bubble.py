#Bubble sort method

numbers = [1,8,6,4,3,10,2]

length = len(numbers)-1

#iterations needed
for i in range(length):
    #restart variables
    a = 0
    b = 1
    #compare each value of the array
    for j in range(length):
        if numbers[a]>numbers[b]:
            numbers[a],numbers[b] = numbers[b],numbers[a]
        a +=1
        b +=1
    length -=1

print(numbers)

