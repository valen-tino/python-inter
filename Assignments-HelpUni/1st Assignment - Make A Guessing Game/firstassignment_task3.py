# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 3 (Player vs Computer)

from random import randint

def main():
    mainPlayer,comp = "Player","Computer"
    totalGuess = 1
    mini,max = 0,100
    num = randint(mini, max)
    player = mainPlayer

    print("Player: "+player)
    guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))

    while (totalGuess):
        
        if player == mainPlayer:
            player = comp
            if guessedNum == num:   
                player = mainPlayer                        
                print("\n",player,"wins")
                exit() 
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
                    
        if player == comp:
            player = mainPlayer
            computerResult = randint(mini,max)

            def compShow(mini,max,computerResult):
                var_low,var_high = mini,max
                results = computerResult
                var = print("Number ranges from "+str(var_low)+" to "+str(var_high)+".")
                var = print('Computer choose',results)
                return var

            if computerResult == num:  
                player = comp
                compShow(mini,max,computerResult)                       
                print("\n",player,"wins") 
                exit() 
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
            
        guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))

main()
