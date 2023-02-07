import random

print(
    '''
    +================================+
    |      Welcome to my game!       |
    |  Enter an integer number and   |
    | guess the number I've  picked  |
    |      picked for you...         |
    | So, what is the secret number? |
    +================================+
    '''
)


number = int(random.randint(0, 1000))
#print(number)
guess = int( input('Enter your guess: '))
counter = 1
giveUp = 0

if (guess != number):
    print('Ups, looks like you did not got it right... Try again')
    while (guess != number or giveUp== 0):
        if(guess > number):
            print('Too high, try to lower your guess')
            guess = int( input('Enter your guess: '))
        elif(guess < number):
            print('Too low, try to upper your guess')
            guess = int( input('Enter your guess: '))
        counter +=1
        if(counter == 10 or counter == 20):
            giveUp= int(input('Do you give up? If you do type 1, if you wanna keep guessing type 0 '))
            if(giveUp == 1):
                print('The secret number was: ', number, '\nThanks for playing')
                break
    if (guess == number):
        print('Congratulations, you guess the number!!!')        
else:
    print('Congratulations, you guess the number!!!')


