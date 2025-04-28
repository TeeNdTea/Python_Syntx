#check whether a letter is vowel or consonent

#vowel- a, e, i, o, u

word=(input("Enter a letter:"))

if 'a'<=word<='z' or 'A'<=word<='Z': #check if letter
    
    if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u' or word == 'A' or word == 'E' or word == 'I' or word == 'O' or word == 'U':
        print("Vowel")
    else:
        print("Consonent")
else:
    print('Input is invalid')