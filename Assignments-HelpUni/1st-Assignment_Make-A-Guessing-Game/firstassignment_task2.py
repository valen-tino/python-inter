# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 2 (Player vs Player)

from random import randint

#This code is used as the main function to run the game
def main():
    player1,player2 = "Player 1","Player 2"
    low_value,max_value = 0,100
    currentPlayer = player1
    
    # This code is used to get a random number, which number will be used as the answer for the game
    randNum = randint(low_value, max_value)

    #This code is used to insert the player's guess number for the first time
    print(currentPlayer) 
    playerGuessNumber = int(input("Number ranges from "+str(low_value)+" to "+str(max_value)+".\nWhat is your guess? "))

    #This code is used to run the game on loop sequence 
    while True:

        # This code runs when the result from one of the players matches with the final answer from the game
        if playerGuessNumber == randNum:
            print("\nCongratulations! ",currentPlayer, "wins")

            # This code is used to end the game
            exit()
        
        # This code is used to select when it's the first player's turn
        elif currentPlayer == player1:

            #This code is used to switch turns from player1 to player2 after the game displays the result
            currentPlayer = player2

            # This code validates the player's answer and compares it with the answer of the game
            if playerGuessNumber < low_value or playerGuessNumber > max_value: 
                print('Incorrect!\n')

            #This code is used to increase/decrease the range each time player1 enters their guessed number
            elif playerGuessNumber < randNum:
                low_value = playerGuessNumber + 1
                print('Incorrect!\n')
            else:
                max_value = playerGuessNumber - 1
                print('Incorrect!\n')
        
        # This code is used to select when it's the second player's turn
        elif currentPlayer == player2:

            #This code is used to switch turns from player2 to player1 after the game displays the result
            currentPlayer = player1
            # This code validates the player's answer and compares it with the answer of the game
            if playerGuessNumber < low_value or playerGuessNumber > max_value: 

                #This code will display "Incorrect" if the player's guess isn't the same as the answer
                print('Incorrect!\n')

            #This code is used to increase/decrease the range each time player2 enters their guessed number
            elif playerGuessNumber < randNum:
                low_value = playerGuessNumber + 1
                print('Incorrect!\n')
            else:
                max_value = playerGuessNumber - 1
                print('Incorrect!\n')
        
        #This code displays the current player
        print(currentPlayer)

        #This code is used to insert the player's guess number everytime the player's turn
        playerGuessNumber = int(input("Number ranges from "+str(low_value)+" to "+str(max_value)+".\nWhat is your guess? "))

main()
