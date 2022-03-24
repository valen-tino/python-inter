# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 2 (Player vs Player)

from random import randint

# Main Function
def main():
    player1,player2 = "Player 1","Player 2"
    totalGuess = 1
    mini,max = 0,100
    num = randint(mini, max)
    player = player1

    print(player) # Only for testing purposes
    guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))

    while (totalGuess):
        if guessedNum == num:
            print("\nCongratulations! ",player, "wins")
            exit()
            
        elif player == player1:
            player = player2
            if guessedNum < mini or guessedNum > max: 
                print('Incorrect!\n')
            elif guessedNum < num:
                mini = guessedNum + 1
                print('Incorrect!\n')
            else:
                max = guessedNum - 1
                print('Incorrect!\n')
    
        elif player == player2:
            player = player1
            if guessedNum < mini or guessedNum > max: 
                print('Incorrect!\n')
            elif guessedNum < num:
                mini = guessedNum + 1
                print('Incorrect!\n')
            else:
                max = guessedNum - 1
                print('Incorrect!\n')
        
        print(player)
        guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))

main()
