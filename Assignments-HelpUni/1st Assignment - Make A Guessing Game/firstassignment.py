# Imports "random" library for the code to work.
import random

# The default value since the user didn't input any number yet.
totalGuesses = 0

# Generate a random range for the user to guess.
min = random.randint(1,100)
max = random.randint(1,100)

# Chooses a random number from the range for the user to guess.
number = random.randint(min, max)

# Displays the range of the number to guess
print('Number ranges from '+str(min)+' to '+str(max))

# Initiate the loop sequence to make sure that it repeats when the user inserts the incorrect answer
while totalGuesses != number:
    print("Number : "+str(number))
    guess = eval(input("What is your guess? "))
    guess = int(guess)

    totalGuesses = totalGuesses + 1

    # It Will display the text below if the user submits the incorrect number.
    if guess != number:
        print('Incorrect!')

    # It Will display the text below if the user submits the number correctly.
    if guess == number:
        
        # It will display the text below if user submits the number correctly for less than 5 tries.
        if totalGuesses < 5:  
            print('Congratulation! You have done it in ' + str(totalGuesses) + ' tries!')
            print('You are lucky today!')

        # It Will display the text below if the user submits the number correctly for more than 5 tries.
        else:
            print('Congratulation! You have done it in ' + str(totalGuesses) + ' tries!')
        break

