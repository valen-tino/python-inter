# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 2 (Player vs Player)

from random import randint

# Main Function
def main():
    player1,player2 = "Player 1","Player 2"
    low_value,max_value = 0,100
    randNum = randint(low_value, max_value)
    currentPlayer = player1

    #This code is used to insert the player's guess number for the first time
    print(currentPlayer) 
    playerGuessNumber = int(input("Number ranges from "+str(low_value)+" to "+str(max_value)+".\nWhat is your guess? "))

    #The totalGuess's fixed variable is used to activate the codes below
    while True:
        # This code runs when the result from one of the players matches with the answer
        if playerGuessNumber == randNum:
            print("\nCongratulations! ",currentPlayer, "wins")
            exit()
        
        # This code runs when it's the first player's turn
        elif currentPlayer == player1:
            currentPlayer = player2
            # This code validates the player's answer and compares it with the answer of the game
            if playerGuessNumber < low_value or playerGuessNumber > max_value: 
                print('Incorrect!\n')
            elif playerGuessNumber < randNum:
                low_value = playerGuessNumber + 1
                print('Incorrect!\n')
            else:
                max_value = playerGuessNumber - 1
                print('Incorrect!\n')
        
        # This code runs when it's the second player's turn
        elif currentPlayer == player2:
            currentPlayer = player1
            # This code validates the player's answer and compares it with the answer of the game
            if playerGuessNumber < low_value or playerGuessNumber > max_value: 
                print('Incorrect!\n')
            elif playerGuessNumber < randNum:
                low_value = playerGuessNumber + 1
                print('Incorrect!\n')
            else:
                max_value = playerGuessNumber - 1
                print('Incorrect!\n')
        
        #This code is used to insert the player's guess number everytime the player's turn
        print(currentPlayer)
        playerGuessNumber = int(input("Number ranges from "+str(low_value)+" to "+str(max_value)+".\nWhat is your guess? "))

main()
