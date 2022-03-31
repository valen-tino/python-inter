# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 1
from random import randint

# This code is used as the main function of the game
def main():
    totalGuesses = 1
    low_value,max_value = 0,100

    # This code is used to get a random number, which number will be used as the answer for the game
    randNum = randint(low_value, max_value)

    #This code is used to insert the player's guess number for the first time
    playerGuessNumber = int(input("Range "+str(low_value)+" --> "+str(max_value)+". Your guess? "))
    
    # This code validates the player's answer and compares it with the answer of the game
    while playerGuessNumber != randNum:

        #This code is used to reject player's guess if the player's guess is above/below the current min & max value
        if playerGuessNumber < low_value or playerGuessNumber > max_value:
            print('Incorrect!\n')

        #This code is used to increase/decrease the range each time the player enters their guessed number
        elif playerGuessNumber < randNum:
            low_value = playerGuessNumber + 1
            print('Incorrect!\n')
        else:
            max_value = playerGuessNumber - 1
            print('Incorrect!\n')

        #This code is used to insert the player's guess number everytime the player's turn
        playerGuessNumber = int(input("Range "+str(low_value)+" --> "+str(max_value)+". Your guess? "))
        
        #This code is used to repeat the player's turn each time the player tries to input the guessed number
        totalGuesses+=1

    #This code checks the player's total guess and displays how many tries did the user try to get the answer. And, if the player's tries is less than 5 tries, it will display that the player is lucky today.
    if totalGuesses < 5:
        print('\nCongratulation! You have done it in ' + str(totalGuesses) + ' tries!')
        print('You are lucky today!')
    else:
        print('\nCongratulation! You have done it in ' + str(totalGuesses) + ' tries!')
          
main()
