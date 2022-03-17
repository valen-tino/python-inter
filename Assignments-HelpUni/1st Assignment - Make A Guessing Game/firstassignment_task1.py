# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 1

# Import Random Library
import random

# Global Variables
totalGuesses = 1
mini,max = 0,100
num = random.randint(mini, max)

# Function to show range
def range(mini,max):
    a,b = mini,max
    return int(input("Range "+str(a)+" --> "+str(b)+" . Your guess? "))

# Main Function
def main():
    # Calls the global variables to be used in the main() function
    global totalGuesses,mini,max,num

    print("Debug Guess : "+str(num)) # Only for testing purposes
    guessedNum = range(mini,max)
    
    while guessedNum != num:
        if guessedNum < mini or guessedNum > max:
            print('Incorrect!\n')
            guessedNum = range(mini,max)

        elif guessedNum < num:
            mini = guessedNum + 1
            print('Incorrect!\n')
            guessedNum = range(mini,max)

        else:
            max = guessedNum - 1
            print('Incorrect!\n')
            guessedNum = range(mini,max)

        totalGuesses+=1

    if guessedNum == num:
        if totalGuesses < 5:  
            print('\nCongratulation! You have done it in ' + str(totalGuesses) + ' tries!')
            print('You are lucky today!')
            exit()
        else:
            print('\nCongratulation! You have done it in ' + str(totalGuesses) + ' tries!')
            exit()

main()
