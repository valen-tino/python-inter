import random
#generate number directly
num = random.randrange(1,5)

#initialize global variables
player1 = "Human"
player2 = "Alien"
player = ""
player1PlayCount = 0
player2PlayCount = 0
maxPlayTimes = 3

#game logic
def Game():
    global player1, player2, player, player1PlayCount, player2PlayCount, maxPlayTimes, num
    """enter and assign names to players"""
    player1Name = input('Player1 Enter Your Name: ')
    player2Name = input('Player2 Enter Your Name: ')
    
    player1 = player1Name
    
    player2 = player2Name
    
    player = player1
    
    print(player1, 'turn')
    
    while ((player1PlayCount and player2PlayCount) != maxPlayTimes):
        guessNum = int(input("Guess Number: "))

        if guessNum == num:
            print(player, "won")
            exit()
            
        elif player == player1:
            player1PlayCount +=1
            player = player2
            print(player2, 'turn')
            
        elif player == player2:
            player2PlayCount +=1
            player = player1
            print(player1, 'turn')

        else:
            print("Both ", player1, " and ", player2, " lose")
            exit()
Game()