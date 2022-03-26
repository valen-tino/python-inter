# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 5 (Player vs Computer with Game Sessions and custom functions)

from random import randint

def dealWithATurn(currentUser,low_value,max_value):
    #This code chooses when
    if currentUser == "Player":
        currentGuess = eval(input("Your guess? "))
    elif currentUser == "Computer":
        currentGuess = randint(low_value,max_value)
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
        low_value,max_value = 0,100
        randNum = randint(low_value, max_value)

        # This code displays the current game
        print("Game:",str(var_game))
        while currentGuess != randNum:
            
            if counts%2 == 0:
                currentUser = player
            else:
                currentUser = comp
            
            print("Debug Number:",randNum)
            print("Player:",currentUser)
            print("Range "+str(low_value)+" --> "+str(max_value)+".",end = ' ')
            currentGuess = dealWithATurn(currentUser,low_value,max_value)

            counts = counts + 1

            if currentGuess < randNum:
                low_value = currentGuess + 1
            if currentGuess > randNum:
                max_value = currentGuess - 1
            if currentGuess != randNum:
                print("Incorrect!\n")
        
        #
        print(currentUser,"wins\n")
        if currentUser == player:
            countScorePlayer = countScorePlayer + 1
        elif currentUser == comp:
            countScoreComp = countScoreComp + 1

        if countScorePlayer == 3 or countScoreComp == 3:
            
            displayFinalResult(countScorePlayer,countScoreComp)
            exit()

        var_game+=1
            
main()