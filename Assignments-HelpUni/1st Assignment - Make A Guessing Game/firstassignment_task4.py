# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 4 (Player vs Computer with Game Sessions)

import random

def main():
    var_game = 1
    player,comp = "Player","Computer"
    countScorePlayer = 0
    countScoreComp = 0

    # This code is used to run the game on loop sequence 
    while True:
        currentGuess,counts = -1,0
        low_value,max_value = 0,100
        randNum = random.randint(low_value, max_value)

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
            if currentUser == player:
                currentGuess = eval(input("Your guess? "))
            elif currentUser == comp:
                currentGuess random.randint(low_value,max_value)
                print("Computer guess "+str(currentGuess))
            
            #
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
            #
            print("Score: 'Human': "+str(countScorePlayer)+" 'Computer': "+str(countScoreComp)+".",end = ' ')
            if countScorePlayer > countScoreComp:
                print("Winner is Player")
            else:
                print("Winner is Computer")
            break

        var_game+=1
            
main()
