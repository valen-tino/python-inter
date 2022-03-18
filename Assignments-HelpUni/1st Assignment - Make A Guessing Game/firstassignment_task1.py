# Guess The Number!
# Valentino Yudhistira Jehaut
# E2100312
# Assignment 1
# Task 1
from random import randint

# Main Function
def main():
    totalGuesses,mini,max = 1,0,100
    num = randint(mini, max)
    guessedNum = int(input("Range "+str(mini)+" --> "+str(max)+" . Your guess? "))
    
    while guessedNum != num:
        if guessedNum < mini or guessedNum > max:
            print('Incorrect!\n')
            guessedNum = int(input("Range "+str(mini)+" --> "+str(max)+" . Your guess? "))

        elif guessedNum < num:
            mini = guessedNum + 1
            print('Incorrect!\n')
            guessedNum = int(input("Range "+str(mini)+" --> "+str(max)+" . Your guess? "))

        else:
            max = guessedNum - 1
            print('Incorrect!\n')
            guessedNum = int(input("Range "+str(mini)+" --> "+str(max)+" . Your guess? "))

        totalGuesses+=1

    if (not guessedNum == num) or (not totalGuesses < 5):
            print('\nCongratulation! You have done it in ' + str(totalGuesses) + ' tries!')
    print('\nCongratulation! You have done it in ' + str(totalGuesses) + ' tries!')
    print('You are lucky today!')
       
main()
