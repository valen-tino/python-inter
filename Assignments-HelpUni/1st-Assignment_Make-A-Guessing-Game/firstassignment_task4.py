# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 4 (Player vs Computer with Game Sessions)

#This code is used to import the function "randint" from the "random library"
from random import randint

#This code is used as the main function to run the game
def main():
    var_game = 1
    player,comp = "Player","Computer"
    currentPlayerScore = 0
    currentCompScore = 0
    theWinner = player
    keep_playing = "True"

    while keep_playing == "True":
        currentGuess = -1
        totalCounts = 0
        low_value,max_value = 0,100

        # This code is used to get a random number, which number will be used as the answer for the current game session
        randomNumber = randint(low_value, max_value)

        # This code displays the current game session
        print("Game:",str(var_game))
        while currentGuess != randomNumber:
            
            # This code is used to switch positions if the player/computer wins
            if theWinner == player:
                # This code is used to detect if the current turn is player or computer
                if totalCounts%2 == 0:
                    currentUser = player
                else:
                    currentUser = comp
            else:
                # This code is used to detect if the current turn is player or computer
                if totalCounts%2 == 0:
                    currentUser = comp
                else:
                    currentUser = player
        
            print("Debug Number:",randomNumber) # Testing Only

            #This code displays the current user and the range of the answer
            print("Player:",currentUser)
            print("Range "+str(low_value)+" --> "+str(max_value)+".",end = ' ')

            #This code is used to ask the player/computer for input which will be used to guess the answer from this game session
            if currentUser == player:

                #This code is used for the player to guess the the answer from this game session
                currentGuess = eval(input("Your guess? "))

            elif currentUser == comp:
                
                #This code is used for the computer to guess the answer from this game session
                currentGuess = randint(low_value,max_value)
                print("Computer guess "+str(currentGuess))
            
            #This code is used to increase/decrease the range each time the player/computer enters their guessed number
            if currentGuess < randomNumber:
                low_value = currentGuess + 1
            if currentGuess > randomNumber:
                max_value = currentGuess - 1
            if currentGuess != randomNumber:
                print("Incorrect!\n")

            #This code is used to repeat the turn if the player/computer has entered their answer
            totalCounts = totalCounts + 1

        #This code used to show if the player/computer wins the current game session
        print(currentUser,"wins\n")

        # This code is used to get the theWinner of the current game session 
        # and the theWinner of the current game session will be the first to start at the next game session
        theWinner = currentUser
        
        #This code is used to add a score whenever the player/computer wins on each turn
        if currentUser == player:
            currentPlayerScore = currentPlayerScore + 1
        elif currentUser == comp:
            currentCompScore = currentCompScore + 1

        #This code is used if the player/computer score is already 3 turns
        if currentPlayerScore == 3 or currentCompScore == 3:
            
            #This code displays the total score of both the player and the computer 
            print("Score: 'Human': "+str(currentPlayerScore)+" 'Computer': "+str(currentCompScore)+".",end = ' ')

            #This code is used to decide the theWinner and displays the final decision if one of them is the theWinner
            if currentPlayerScore > currentCompScore:
                print("Winner is Player")
            else:
                print("Winner is Computer")
            
            #This code is used to end the game
            keep_playing = "False"

        #This code is used to repeat the game session if the player/computer turn is already done
        var_game+=1
            
main()