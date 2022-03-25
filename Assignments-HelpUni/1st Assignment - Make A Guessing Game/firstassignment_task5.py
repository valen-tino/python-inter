# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 5 (Player vs Computer with Game Sessions)

from random import randint

def dealWithATurn(currentUser,start,end):
    player,comp = "Player","Computer"
    randNum = randint(start,end)

    if currentUser == player:
        currentGuess = eval(input("Your guess? "))
    elif currentUser == comp:
        currentGuess = randint(low_value,max_value)
        print("Computer guess "+str(currentGuess))
    
    counts = counts + 1
    if currentGuess < randNum:
        low_value = currentGuess + 1
    if currentGuess > randNum:
        max_value = currentGuess - 1
    if currentGuess != randNum:
        print("Incorrect!\n")

def displayFinalResult(pSC,cSC):
    print("Score: 'Human': "+str(pSC)+" 'Computer': "+str(cSC)+".",end = ' ')
    if pSC > cSC:
        print("Winner is Player")
    else:
        print("Winner is Computer")

def main():
    var_game = 1
    player,comp = "Player","Computer"
    playerScoreCount = 0
    compScoreCount = 0

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

            #This code displays the current player and the range of the answer
            print("Player:",currentUser)
            print("Range "+str(low_value)+" --> "+str(max_value)+".",end = ' ')

            #This code chooses when
            dealWithATurn(currentUser,low_value,max_value)
        
        #
        print(currentUser,"wins\n")
        if currentUser == player:
            playerScoreCount = playerScoreCount + 1
        elif currentUser == comp:
            compScoreCount = compScoreCount + 1

        if playerScoreCount == 3 or compScoreCount == 3:
            #
            displayFinalResult(playerScoreCount,compScoreCount)
            break

        var_game+=1
            
main()
