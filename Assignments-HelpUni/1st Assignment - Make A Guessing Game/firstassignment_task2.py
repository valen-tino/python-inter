# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 2 (Player vs Player)

from random import randint

# Main Function
def main():
    player1,player2 = "Player 1","Player 2"
    totalGuess,mini,max = 1,0,100
    num,player = randint(mini, max),player1

    print("\nDebug Guess : "+str(num)+"\n"+player) # Only for testing purposes
    guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))

    while (totalGuess):
        if guessedNum == num:
            print("\nCongratulations! ",player, "wins")
            exit()
            
        elif player == player1:
            player = player2
            if guessedNum < mini or guessedNum > max: 
                print('Incorrect!\n')
                print(player)
                guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))

            elif guessedNum < num:
                mini = guessedNum + 1
                print('Incorrect!\n')
                print(player)
                guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))

            else:
                max = guessedNum - 1
                print('Incorrect!\n')
                print(player)
                guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))
    
        elif player == player2:
            player = player1
            if guessedNum < mini or guessedNum > max: 
                print('Incorrect!\n')
                print(player)
                guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))

            elif guessedNum < num:
                mini = guessedNum + 1
                print('Incorrect!\n')
                print(player)
                guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))

            else:
                max = guessedNum - 1
                print('Incorrect!\n')
                print(player)
                guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))
    
main()
