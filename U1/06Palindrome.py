#Determine if a word or sentence is a palindrome

chars = ['.', ',', '!', '¿','?',"’"]

input = input('Enter a word or sentence: ')

word = input.replace(" ", " ")
word = word.lower()
word = word.translate(str.maketrans('', '', ''.join(chars)))


length = (len(word)//2)
p=0
n= len(word)-1
c=0

for i in range(length):
    if word[p] == word[n]:
        c += 1
    p+=1
    n-=1

if c == length:
    print('Yes, this is a palindrome')
else:
    print('No, this is not a palindrome')

