import random

def main():
    totalGuesses = 0
    min = 0
    max = 100

    number = random.randint(min, max)
    print("Debug Guess : "+str(number)) # Only for testing purposes
    guessedNum = int(input("Range "+str(min)+" --> "+str(max)+" . Your guess? "))

    while guessedNum != number:
        if guessedNum < min or guessedNum > max:
            print('Incorrect!')
            guessedNum = int(input("Range "+str(min)+" --> "+str(max)+" . Your guess? "))
        elif guessedNum < number:
            min = guessedNum + 1
            print('Incorrect!')
            guessedNum = int(input("Range "+str(min)+" --> "+str(max)+" . Your guess? "))
        elif guessedNum > number:
            max = guessedNum - 1
            print('Incorrect!')
            guessedNum = int(input("Range "+str(min)+" --> "+str(max)+" . Your guess? "))
        else:
            print("Invalid Input, Try Again")
            guessedNum = int(input("Range "+str(min)+" --> "+str(max)+" . Your guess? "))

        totalGuesses+=1

    if guessedNum == number:
        if totalGuesses < 5:  
            print('Congratulation! You have done it in ' + str(totalGuesses) + ' tries!')
            print('You are lucky today!')
        else:
            print('Congratulation! You have done it in ' + str(totalGuesses) + ' tries!')

main()