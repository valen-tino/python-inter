# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 3 (Player vs Computer)

from random import randint

def main():
    player,comp = "Player","Computer"
    low_value,max_value = 0,100
    randNum = randint(low_value, max_value)
    currentUser = player

    #This code is used to insert the player's guess number for the first time   
    print("Debug Number:",randNum)
    print("Player: "+currentUser)
    playerGuessNumber = int(input("Number ranges from "+str(low_value)+" to "+str(max_value)+".\nWhat is your guess? "))

    #The totalGuess's fixed variable is used to activate the codes below
    while True:
        
        # This code runs when it's the player's turn
        if currentUser == player:
            currentUser = comp

            # This code validates the player's answer and compares it with the answer of the game
            if playerGuessNumber == randNum:   
                currentUser = player                        
                print("\n"+currentUser+" wins")
                exit() 
            elif playerGuessNumber < low_value or playerGuessNumber > max_value: 
                print('Incorrect!\n')
                print('Player:',currentUser)
            elif playerGuessNumber < randNum:
                low_value = playerGuessNumber + 1
                print('Incorrect!\n')
                print('Player:',currentUser)
            else:
                max_value = playerGuessNumber - 1
                print('Incorrect!\n')
                print('Player:',currentUser)

        # This code runs when it's the computer's turn            
        if currentUser == comp:
            currentUser = player
            computerResult = randint(low_value,max_value)

            # Function to show the result from the computer
            def compShow(low_value,max_value,computerResult):
                print("Number ranges from "+str(low_value)+" to "+str(max_value)+".")
                print('Computer guess',computerResult)

            # This code validates the computer's answer and compares it with the answer of the game
            if computerResult == randNum:  
                currentUser = comp
                compShow(low_value,max_value,computerResult)                       
                print("\n"+currentUser+" wins") 
                exit() 
            elif computerResult < low_value or computerResult > max_value: 
                compShow(low_value,max_value,computerResult)                       
                print('Incorrect!\n')
                print('Player:',currentUser)
            elif computerResult < randNum:
                low_value = computerResult + 1
                compShow(low_value,max_value,computerResult)                       
                print('Incorrect!\n')
                print('Player:',currentUser)
            else:
                max_value = computerResult - 1
                compShow(low_value,max_value,computerResult)                       
                print('Incorrect!\n')
                print('Player:',currentUser)

        #This code is used to insert the player's guess number everytime the player's turn   
        playerGuessNumber = int(input("Number ranges from "+str(low_value)+" to "+str(max_value)+".\nWhat is your guess? "))

main()
