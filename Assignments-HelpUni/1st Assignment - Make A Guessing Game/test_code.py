"""This game generates random number, then players try to guess the number generated"""

import random

def Game():
    Guess = 0
    NumberOfGuesses = 0
    NumberToGuess = int(input("Player One enter you chosen number: "))
    while NumberToGuess < 1 or NumberToGuess > 10:
        NumberToGuess = int(input("Not a valid choice, please enter another number: "))
    while Guess != NumberToGuess and NumberOfGuesses < 5:
        Guess = int(input("Player Two have a guess: "))
        NumberOfGuesses = NumberOfGuesses + 1
    if Guess == NumberToGuess:
        print("Player Two wins.")
    else:
        print("Player One wins.")


Game()