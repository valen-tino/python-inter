# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 3 (Player vs Computer)

from random import randint

# Main Function
def computer_guess(num):
    low = 1
    high = 100
    guess = (low+high)//2
    while guess != num:
        guess = (low+high)//2
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")


def main():
    player1,comp = "Player 1","Computer"
    totalGuess,mini,max = 1,0,100
    num,player = randint(mini, max),player1

    print("\nDebug Guess : "+str(num)+"\n"+player) # Only for testing purposes
    guessedNum = int(input("Number ranges from "+str(mini)+" to "+str(max)+".\nWhat's your guess? "))

    while (totalGuess):
        if guessedNum == num:                            
            print("\nCongratulations! ",player, "wins")
            exit()
            
        elif player == player1:z
            player = comp
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
    
        elif player == comp:
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
