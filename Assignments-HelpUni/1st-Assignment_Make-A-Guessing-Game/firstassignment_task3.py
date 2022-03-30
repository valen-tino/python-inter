# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 3 (Player vs Computer)

#This code is used to import the function "randint" from the "random library"
from random import randint

#This code is used as the main function to run the game
def main():
    player,comp = "Player","Computer"
    low_value,max_value = 0,100
    currentUser = player
    keep_playing = "True"

    # This code is used to get a random number, which number will be used as the answer for the game
    randNum = randint(low_value, max_value)

    #This code is used to show the current turn insert the player's guess number for the first time   
    print("Debug Number:",randNum)
    print("Player: "+currentUser)
    playerGuessNumber = int(input("Number ranges from "+str(low_value)+" to "+str(max_value)+".\nWhat is your guess? "))

    #This code is used to run the game on loop sequence 
    while keep_playing == "True":
        
        # This code is used to select when it's the player's turn
        if currentUser == player:

            #This code is used to switch turns from player to computer after the game shows the results
            currentUser = comp

            # This code validates the player's answer and compares it with the answer of the game
            if playerGuessNumber == randNum:   

                #This code is used change turns from player to computer after the game shows the results
                currentUser = player           

                #This code used to show if the player wins the current game session
                print("\n"+currentUser+" wins")

                #This code is used to end the game
                keep_playing == "False" 

            #This code is used to reject player's guess if the min & max value is above the current min & max value
            elif playerGuessNumber < low_value or playerGuessNumber > max_value: 
                print('Incorrect!\n')

                #This code is used to show the next user's turn
                print('Player:',currentUser)

            #This code is used to increase/decrease the range each time the player enters their guessed number
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
            #This code is used change turns from player to computer after the game shows the results
            currentUser = player

            #This code is used for the computer to guess the the answer from this game session
            computerResult = randint(low_value,max_value)

            #This code is used as a function for the computer to guess the answer from this game session
            def compShow(low_value,max_value,computerResult):
                print("Number ranges from "+str(low_value)+" to "+str(max_value)+".")
                print('Computer guess',computerResult)

            # This code validates the computer's answer and compares it with the answer of the game
            if computerResult == randNum:  

                #This code is used change turns from computer to player after the game shows the results
                currentUser = comp

                #This code function is used for the computer to guess the answer from this game session
                compShow(low_value,max_value,computerResult)   

                #This code used to show if the computer wins the game                     
                print("\n"+currentUser+" wins") 

                #This code is used to end the game
                keep_playing == "False" 
            
            #This code is used to reject computer's guess if the min & max value is above the current min & max value
            elif computerResult < low_value or computerResult > max_value: 
                compShow(low_value,max_value,computerResult)                       
                print('Incorrect!\n')

                #This code is used to show the next user's turn
                print('Player:',currentUser)

            #This code is used to increase/decrease the range each time the computer enters their guessed number
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
