# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 1
from random import randint

# Main Function
def main():
    totalGuesses = 1
    low_value,max_value = 0,100

    # This code is used to get a random number, which number will be used as the answer for the game
    randNum = randint(low_value, max_value)

    #This code is used to insert the player's guess number for the first time
    playerGuessNumber = int(input("Range "+str(low_value)+" --> "+str(max_value)+". Your guess? "))
    
    # This code validates the player's answer and compares it with the answer of the game
    while playerGuessNumber != randNum:
        if playerGuessNumber < low_value or playerGuessNumber > max_value:
            print('Incorrect!\n')
        elif playerGuessNumber < randNum:
            low_value = playerGuessNumber + 1
            print('Incorrect!\n')
        else:
            max_value = playerGuessNumber - 1
            print('Incorrect!\n')

        #This code is used to insert the player's guess number everytime the player's turn
        playerGuessNumber = int(input("Range "+str(low_value)+" --> "+str(max_value)+". Your guess? "))
        totalGuesses+=1

    #This code val
    # idates the guessed Number and checks
    if totalGuesses < 5:
        print('\nCongratulation! You have done it in ' + str(totalGuesses) + ' tries!')
        print('You are lucky today!')
    else:
        print('\nCongratulation! You have done it in ' + str(totalGuesses) + ' tries!')
          
main()
