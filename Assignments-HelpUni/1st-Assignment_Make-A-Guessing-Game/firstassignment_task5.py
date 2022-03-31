# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 5 (Player vs Computer with Game Sessions and custom functions)

#This code is used to import the function "randint" from the "random library"
from random import randint

#This code is used as a function to display input for players or display input from the computer based on the current turn
def dealWithATurn(currentPlayer,start,end): 

    #This code displays the current user and the range of the answer
    print("Player:",currentPlayer)
    print("Range "+str(start)+" --> "+str(end)+".",end = ' ')

    #This code is used to ask the player/computer for input which will be used to guess the answer from this game session
    if currentPlayer == "Player":
        currentGuess = eval(input("Your guess? "))
    elif currentPlayer == "Computer":

        #This code is used for the computer to guess the answer from this game session
        currentGuess = randint(start,end)
        print("Computer guess "+str(currentGuess))

    #This code is used to get the current guess of player/computer and returns the guess to the main function
    return currentGuess

# This code is used as a function to display the total score of player/computer from 
# all the game sessions and displays the result if one of them is the winner in this game.
def displayFinalResult(currentPlayerScore,currentCompScore): 

    #This code displays the total score of both the player and the computer 
    print("Score: 'Human': "+str(currentPlayerScore)+" 'Computer': "+str(currentCompScore)+".",end = ' ')

    #This code is used to decide the winner and displays the final decision if one of them is the winner
    if currentPlayerScore > currentCompScore:
        print("Winner is Player")
    else:
        print("Winner is Computer")

#This code is used as the main function to run the game
def main():
    var_game = 1
    player,comp = "Player","Computer"
    currentPlayerScore = 0
    currentCompScore = 0
    
    keep_playing = "True"
    theWinner = player

    # This code is used to run the game on loop sequence 
    while keep_playing == "True":
        currentGuess = -1
        totalCounts = 0
        start,end = 0,100

        #This code is used to get a random number, which number will be used as the answer for the current game session
        randomNumber = randint(start, end)

        # This code displays the current game session
        print("Game:",str(var_game))

        #This code is used to run the game if the player/computer guessed number isn't the same as the answer
        while currentGuess != randomNumber:
            
            # This code is used to switch positions if the player/computer wins
            if theWinner == comp:
                # This code is used to detect if the current turn is player or computer
                if totalCounts%2 == 0:
                    currentPlayer = comp
                else:
                    currentPlayer = player
            else:
                # This code is used to detect if the current turn is player or computer
                if totalCounts%2 == 0:
                    currentPlayer = player
                else:
                    currentPlayer = comp
                    
            #This code displays the current player and the range of the answer
            print("Debug Number:",randomNumber)

            #This code function is used to display the last score of the player/computer and display the result if one of them is the winner in this game.
            currentGuess = dealWithATurn(currentPlayer,start,end)

            #This code is used to increase/decrease the range each time the player/computer enters their guessed number            
            if currentGuess < randomNumber:
                start = currentGuess + 1
            if currentGuess > randomNumber:
                end = currentGuess - 1

            #This code is used to display "Incorrect" if the player/computer guessed number isn't the same as the answer
            if currentGuess != randomNumber:
                print("Incorrect!\n")

            #This code is used to repeat the turn if the player/computer has entered their answer
            totalCounts = totalCounts + 1
        
        #This code used to show if the player/computer wins the current game session
        print(currentPlayer,"wins\n")

        # This code is used to get the winner of the current game session 
        # and the winner of the current game session will be the first to start at the next game session
        winner = currentPlayer

        #This code is used to add a score when the player/computer wins on each turn
        if currentPlayer == player:
            currentPlayerScore = currentPlayerScore + 1
        elif currentPlayer == comp:
            currentCompScore = currentCompScore + 1

        #This code is used if the player/computer score is already 3 turns
        if currentPlayerScore == 3 or currentCompScore == 3:

            #This code function is used to display the total score of player/computer from 
            # all the game sessions and displays the result if one of them is the winner in this game.
            displayFinalResult(currentPlayerScore,currentCompScore)

            #This code is used to end the game
            keep_playing = "False"

        #This code is used to repeat the game session if the player/computer turn is already done
        var_game+=1
            
main()