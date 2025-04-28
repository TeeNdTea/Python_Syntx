'''
start
input guessNumber
generate randomNumber
if guessNumber == randomNumber
    1.yes,won
    2.No,lost
end
'''
# import random   #this has all libraries(takes a lot memory)
# from random import randint  #specifying the function
# guessNumber=int(input('Enter a number between 5: '))
# # randomNumber= random.randint(1,5)   #for shorter range of number
# # randomNumber= random.random()*100   #generating 0-99 any number...for greater range
# randomNumber= randint(1,5)

# if randomNumber == guessNumber:
#     print("Yes,Won!")
# else:
#     print('No,Lost!')



'''
how to access a package:

1. import [package name]
    n = packageName.function
2. from packageName import function
    n = function(parameters)
'''

from random import randint

# Guessing game from 1-5

for i in range(1,6):
    guessNumber = int(input("Enter a number between 1 to 5: "))
    randomNumber = randint(1,6)

    if guessNumber == randomNumber:
        print("Won")
        break
    elif guessNumber>randomNumber:
        print("INVALID INPUT. Number not in range")
    else:
        print("Lost")

print('Random Number is: ',randomNumber)