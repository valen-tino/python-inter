# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 2 (Player vs Player)

from random import randint

# Main Function
def main():
    player1,player2 = "Player 1","Player 2"
    totalGuess = 1
    mini,max = 0,100
    num = randint(mini, max)
    player = player1

    #This code is used to insert the player's guess number for the first time
    print(player) 
    guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat is your guess? "))

    #The totalGuess's fixed variable is used to activate the codes below
    while (totalGuess):
        # This code runs when the result from one of the players matches with the answer
        if guessedNum == num:
            print("\nCongratulations! ",player, "wins")
            exit()
        
        # This code runs when it's the first player's turn
        elif player == player1:
            player = player2
            # This code validates the player's answer and compares it with the answer of the game
            if guessedNum < mini or guessedNum > max: 
                print('Incorrect!\n')
            elif guessedNum < num:
                mini = guessedNum + 1
                print('Incorrect!\n')
            else:
                max = guessedNum - 1
                print('Incorrect!\n')
        
        # This code runs when it's the second player's turn
        elif player == player2:
            player = player1
            # This code validates the player's answer and compares it with the answer of the game
            if guessedNum < mini or guessedNum > max: 
                print('Incorrect!\n')
            elif guessedNum < num:
                mini = guessedNum + 1
                print('Incorrect!\n')
            else:
                max = guessedNum - 1
                print('Incorrect!\n')
        
        #This code is used to insert the player's guess number everytime the player's turn
        print(player)
        guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat is your guess? "))

main()
