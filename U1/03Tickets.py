
amount = int( input('Enter the amount of money that you have: $'))
tickets = 0


while (amount > tickets):
    tickets += 1
    amount -= tickets
    

print('The amount of tickets you can get is: ',tickets , 'tickets')
