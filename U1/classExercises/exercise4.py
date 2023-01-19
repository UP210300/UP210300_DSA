year = int( input('Enter a year: '))

if (year < 1582):
    print('Not within the Gregorian calendar period')
else:
    if ( year%4==0 or year%400==0 or year%100!=0):
        print('The year you enter is a leap year')
    else:
        print('The year you enter is a common year')

