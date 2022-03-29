# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 4 (Player vs Computer with Game Sessions)

from random import randint

def main():
    var_game = 1
    player,comp = "Player","Computer"
    currentPlayerScore = 0
    currentCompScore = 0
    keep_playing = "True"

    # This code is used to run the game on loop sequence 
    while keep_playing == "True":
        currentGuess,counts = -1,0
        low_value,max_value = 0,100
        randNum = randint(low_value, max_value)

        # This code displays the current game
        
        # if currentUser == "wins\n"
        
        print("Game:",str(var_game))
        while currentGuess != randNum:
            
            if var_game%2 == 0:
                if counts%2 == 0:
                    currentUser = comp
                else:
                    currentUser = player
            else:
                if counts%2 == 0:
                    currentUser = player
                else:
                    currentUser = comp
        
            print("Debug Number:",randNum) # Testing Only

            #This code displays the current player and the range of the answer
            print("Player:",currentUser)
            print("Range "+str(low_value)+" --> "+str(max_value)+".",end = ' ')

            #This code is used to show options recieve input if it's the player's turn or 
            if currentUser == player:
                currentGuess = eval(input("Your guess? "))
            elif currentUser == comp:
                currentGuess = randint(low_value,max_value)
                print("Computer guess "+str(currentGuess))
            
            #This code is used to add 
            if currentGuess < randNum:
                low_value = currentGuess + 1
            if currentGuess > randNum:
                max_value = currentGuess - 1
            if currentGuess != randNum:
                print("Incorrect!\n")
            counts = counts + 1

        #This code used to show if the player/computer wins 
        print(currentUser,"wins\n")

        #This code is used to add a score when the player/computer wins on each turn
        if currentUser == player:
            currentPlayerScore = currentPlayerScore + 1
        elif currentUser == comp:
            currentCompScore = currentCompScore + 1

        #This code is used if the player/computer score is already 3
        if currentPlayerScore == 3 or currentCompScore == 3:
            #
            print("Score: 'Human': "+str(currentPlayerScore)+" 'Computer': "+str(currentCompScore)+".",end = ' ')
            if currentPlayerScore > currentCompScore:
                print("Winner is Player")
            else:
                print("Winner is Computer")
            keep_playing = "False"

        var_game+=1
            
main()