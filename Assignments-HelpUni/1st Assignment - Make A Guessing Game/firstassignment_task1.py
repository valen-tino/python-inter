# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 1
from random import randint

# Main Function
def main():
    totalGuesses,mini,max = 1,0,100
    num = randint(mini, max)

    #This code is used to insert the player's guess number for the first time
    guessedNum = int(input("Range "+str(mini)+" --> "+str(max)+". Your guess? "))
    
    # This code validates the player's answer and compares it with the answer of the game
    while guessedNum != num:
        if guessedNum < mini or guessedNum > max:
            print('Incorrect!\n')
        elif guessedNum < num:
            mini = guessedNum + 1
            print('Incorrect!\n')
        else:
            max = guessedNum - 1
            print('Incorrect!\n')

        #This code is used to insert the player's guess number everytime the player's turn
        guessedNum = int(input("Range "+str(mini)+" --> "+str(max)+". Your guess? "))
        totalGuesses+=1

    #This code validates the guessed Number and checks
    if (not guessedNum == num) or (not totalGuesses < 5):
            print('\nCongratulation! You have done it in ' + str(totalGuesses) + ' tries!')
    print('\nCongratulation! You have done it in ' + str(totalGuesses) + ' tries!')
    print('You are lucky today!')
       
main()
