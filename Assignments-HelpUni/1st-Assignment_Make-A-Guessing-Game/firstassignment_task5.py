# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 5 (Player vs Computer with Game Sessions and custom functions)

from random import randint

def dealWithATurn(currentPlayer,start,end): # Done
    print("Player:",currentPlayer)
    print("Range "+str(start)+" --> "+str(end)+".",end = ' ')
    if currentPlayer == "Player":
        currentGuess = eval(input("Your guess? "))
    elif currentPlayer == "Computer":
        currentGuess = randint(start,end)
        print("Computer guess "+str(currentGuess))
    return currentGuess

def displayFinalResult(currentPlayerScore,currentCompScore): # Done
    print("Score: 'Human': "+str(currentPlayerScore)+" 'Computer': "+str(currentCompScore)+".",end = ' ')
    if currentPlayerScore > currentCompScore:
        print("Winner is Player")
    else:
        print("Winner is Computer")

def main():
    var_game = 1
    player,comp = "Player","Computer"
    currentPlayerScore = 0
    currentCompScore = 0
    keep_playing = "True"

    # This code is used to run the game on loop sequence 
    while keep_playing == "True":
        currentGuess,counts = -1,0
        start,end = 0,100
        randNum = randint(start, end)

        # This code displays the current game
        print("Game:",str(var_game))
        while currentGuess != randNum:
            
            if counts%2 == 0:
                currentPlayer = "Player"
            else:
                currentPlayer = "Computer"
            
            print("Debug Number:",randNum)
            currentGuess = dealWithATurn(currentPlayer,start,end)

            counts = counts + 1
            if currentGuess < randNum:
                start = currentGuess + 1
            if currentGuess > randNum:
                end = currentGuess - 1
            if currentGuess != randNum:
                print("Incorrect!\n")
        
        #
        print(currentPlayer,"wins\n")
        if currentPlayer == player:
            currentPlayerScore = currentPlayerScore + 1
        elif currentPlayer == comp:
            currentCompScore = currentCompScore + 1

        if currentPlayerScore == 3 or currentCompScore == 3:
            
            displayFinalResult(currentPlayerScore,currentCompScore)
            keep_playing = "False"

        var_game+=1
            
main()