# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 2

import random

# Global Variable
player1,player2 = "Player 1","Player 2"
totalGuess=1
mini,max = 0,100
num = random.randint(mini, max)

# Function to show the range
def range(mini,max):
    a,b = mini,max
    feedback = print("Number ranges from "+str(a)+" to "+str(b)+".")
    feedback = int(input("What's your guess? "))
    return feedback

# Main Function
def main():
    # Calls the global variables to be used in the main() function
    global mini,max,num,player1,player2,totalGuess

    # makes player1 as default so that everytime the game starts, player 1 will be the first
    player = player1

    print("\nDebug Guess : "+str(num)) # Only for testing purposes

    print(player1)
    guessedNum = range(mini,max)

    while (totalGuess):

        if guessedNum == num:
            print("\nCongratulations! ",player, "wins")
            exit()
            
        elif player == player1:
            player = player2

            if guessedNum < mini or guessedNum > max:
                print('Incorrect!\n',player2)
                guessedNum = range(mini,max)

            elif guessedNum < num:
                mini = guessedNum + 1
                print('Incorrect!\n'+player2)
                guessedNum = range(mini,max)

            else:
                max = guessedNum - 1
                print('Incorrect!\n'+player2)
                guessedNum = range(mini,max)
            
        elif player == player2:
            player = player1

            if guessedNum < mini or guessedNum > max:
                print('Incorrect!\n'+player1)
                guessedNum = range(mini,max)

            elif guessedNum < num:
                mini = guessedNum + 1
                print('Incorrect!\n'+player1)
                guessedNum = range(mini,max)

            else:
                max = guessedNum - 1
                print('Incorrect!\n'+player1)
                guessedNum = range(mini,max)

main()
