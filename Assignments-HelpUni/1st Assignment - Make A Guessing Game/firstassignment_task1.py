# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 1

import random

def range(mini,max):
    a,b = mini,max
    return int(input("Range "+str(a)+" --> "+str(b)+" . Your guess? "))

def main():
    totalGuesses = 1
    mini,max = 0,100

    num = random.randint(mini, max)
    print("Debug Guess : "+str(num)) # Only for testing purposes
    guessedNum = range(mini,max)
    
    while guessedNum != num:
        if guessedNum < mini or guessedNum > max:
            print('Incorrect!')
            guessedNum = range(mini,max)

        elif guessedNum < num:
            mini = guessedNum + 1
            print('Incorrect!')
            guessedNum = range(mini,max)

        else:
            max = guessedNum - 1
            print('Incorrect!')
            guessedNum = range(mini,max)

        totalGuesses+=1

    if guessedNum == num:
        if totalGuesses < 5:  
            print('Congratulation! You have done it in ' + str(totalGuesses) + ' tries!')
            print('You are lucky today!')
        else:
            print('Congratulation! You have done it in ' + str(totalGuesses) + ' tries!')

main()
