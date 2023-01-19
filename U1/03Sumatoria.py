
amount = int( input('Enter the amount the money that you have: $'))
tickets = 0
counter = 1

while (amount > tickets):
    tickets += 1
    amount -= tickets
    counter += 1

print('The amount of tickets you can get is: ',tickets , 'tickets')
