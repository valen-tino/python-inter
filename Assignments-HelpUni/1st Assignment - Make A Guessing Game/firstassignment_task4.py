# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 4 (Player vs Computer with Game Sessions)

from random import randint

# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 3 (Player vs Computer)

from random import randint
from timeit import repeat

def main():
    mainPlayer,comp = "Player","Computer"
    totalGuess = 1
    mini,max = 0,100
    
    var_game = 1
    #This code is used to insert the player's guess number for the first time 
    while var_game < 3:  
        num = randint(mini, max)
        player = mainPlayer
        print("Game",var_game)
        print("Player: "+player)
        guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat is your guess? "))

        #The totalGuess's fixed variable is used to activate the codes below
        while (totalGuess):
            # This code runs when it's the player's turn
            if player == mainPlayer:
                player = comp

                # This code validates the player's answer and compares it with the answer of the game
                if guessedNum == num:   
                    player = mainPlayer                        
                    print("\n"+player+" wins")
                    var_game = var_game + 1 
                    repeat(var_game)
                elif guessedNum < mini or guessedNum > max: 
                    print('Incorrect!\n')
                    print('Player:',player)
                elif guessedNum < num:
                    mini = guessedNum + 1
                    print('Incorrect!\n')
                    print('Player:',player)
                else:
                    max = guessedNum - 1
                    print('Incorrect!\n')
                    print('Player:',player)

            # This code runs when it's the computer's turn            
            if player == comp:
                player = mainPlayer
                computerResult = randint(mini,max)

                # Function to show the result from the computer
                def compShow(mini,max,computerResult):
                    var_low,var_high = mini,max
                    results = computerResult
                    print("Number ranges from "+str(var_low)+" to "+str(var_high)+".")
                    print('Computer guess',results)

                # This code validates the computer's answer and compares it with the answer of the game
                if computerResult == num:  
                    player = comp
                    compShow(mini,max,computerResult)                       
                    print("\n"+player+" wins") 
                    var_game = var_game + 1  
                    repeat(var_game)

                elif computerResult < mini or computerResult > max: 
                    compShow(mini,max,computerResult)                       
                    print('Incorrect!\n')
                    print('Player:',player)
                elif computerResult < num:
                    mini = computerResult + 1
                    compShow(mini,max,computerResult)                       
                    print('Incorrect!\n')
                    print('Player:',player)
                else:
                    max = computerResult - 1
                    compShow(mini,max,computerResult)                       
                    print('Incorrect!\n')
                    print('Player:',player)

            #This code is used to insert the player's guess number everytime the player's turn   
            guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat is your guess? "))

main()
