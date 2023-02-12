#Determine if a word or sentence is a palindrome

#array to remove 
chars = ['.', ',', '!', '¿','?',"’"]

input = input('Enter a word or sentence: ')

#remove space between words, punctuation marks , lower case words
word = input.replace(" "," ")
word = word.lower()
word = word.translate(str.maketrans('', '', ''.join(chars)))

#coparison needed
length = (len(word)%2)
p=0
n= len(word)-1
c=0

#compare the firt and last element of the array
for i in range(length):
    if word[p] == word[n]:
        c += 1 #counter to determine if is palindrome or not
    p+=1
    n-=1

if c == length:
    print('Yes, this is a palindrome')
else:
    print('No, this is not a palindrome')

