# Imports "random" library for the code to work.
import random

def main():
    totalGuesses = 0
    min = 0
    max = 100

    number = random.randint(min, max)
    guessedNum = int(input("Range "+str(min)+" --> "+str(max)+" . Your guess? "))

    while guessedNum != number:
        if guessedNum > number:
            print('Incorrect!')
            totalGuesses = totalGuesses + 1
            temp_max = guessedNum-1
            guessedNum = int(input("Range "+str(min)+" --> "+str(temp_max)+" . Your guess? "))
            
            if guessedNum < number:
                print('Incorrect!')
                totalGuesses = totalGuesses + 1
                temp_min = guessedNum+1
                guessedNum = int(input("Range "+str(temp_min)+" --> "+str(temp_max)+" . Your guess? "))

        elif guessedNum < number:
            print('Incorrect!')
            totalGuesses = totalGuesses + 1
            temp_min = guessedNum+1
            guessedNum = int(input("Range "+str(temp_min)+" --> "+str(temp_max)+" . Your guess? "))

            if guessedNum > number:
                print('Incorrect!')
                totalGuesses = totalGuesses + 1
                temp_max = guessedNum - 1
                guessedNum = int(input("Range "+str(min)+" --> "+str(temp_max)+" . Your guess? "))

    if guessedNum == number:
            
        if totalGuesses < 5:  
            print('Congratulation! You have done it in ' + str(totalGuesses) + ' tries!')
            print('You are lucky today!')

        else:
            print('Congratulation! You have done it in ' + str(totalGuesses) + ' tries!')

main()



