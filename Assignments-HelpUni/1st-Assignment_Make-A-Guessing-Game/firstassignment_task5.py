# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 5 (Player vs Computer with Game Sessions and custom functions)

from random import randint

def dealWithATurn(currentPlayer,start,end):
    print("Player:",currentPlayer)
    print("Range "+str(start)+" --> "+str(end)+".",end = ' ')

    if currentPlayer == "Player":
        currentGuess = eval(input("Your guess? "))
    elif currentPlayer == "Computer":
        currentGuess = randint(start,end)
        print("Computer guess "+str(currentGuess))
    return currentGuess

def displayFinalResult(pSC,cSC): # Done
    print("Score: 'Human': "+str(pSC)+" 'Computer': "+str(cSC)+".",end = ' ')
    if pSC > cSC:
        print("Winner is Player")
    else:
        print("Winner is Computer")

def main():
    var_game = 1
    player,comp = "Player","Computer"
    countScorePlayer = 0
    countScoreComp = 0

    # This code is used to run the game on loop sequence 
    while True:
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
            countScorePlayer = countScorePlayer + 1
        elif currentPlayer == comp:
            countScoreComp = countScoreComp + 1

        if countScorePlayer == 3 or countScoreComp == 3:
            
            displayFinalResult(countScorePlayer,countScoreComp)
            exit()

        var_game+=1
            
main()