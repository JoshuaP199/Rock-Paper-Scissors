from random import *

#1
print("Game: Rock, Paper, Scissors vs a Computer\nThe rules are as follow:")

a = ""
botlist = ("Rock", "Paper", "Scissors")

while True:
    
    while True:

        print("\nChoose either rock (r), paper (p), or scissors (s) and see if you beat the bot")
        print("Please use the () letter corresponding to your response.")
        q = input("What will you choose against the bot? ")
        
        if q == "r":
            a = "Rock"
            break
        elif q == "p":
            a = "Paper"
            break
        elif q == "s":
            a = "Scissors"
            break
        else:
            print('You did not enter a valid letter. Restarting...')
            continue

    b = botlist[randint(0,2)]
    print("\nYou chose " + a + " and the bot chose " + b + ".")
    
    if b == "Rock":
        if a == "Rock":
            print("Its a TIE!")
        elif a == "Paper":
            print("You covered the bot. You WIN!")
        elif a == "Scissors":
            print("The bot smashed you. You Lose.")
    elif b == "Paper":
        if a == "Rock":
            print("The bot covered you. You Lose.")
        elif a == "Paper":
            print("Its a TIE!")
        elif a == "Scissors":
            print("You cut the bot. You WIN!")
    elif b == "Scissors":
        if a == "Rock":
            print("You smashed the bot. You WIN!")
        elif a == "Paper":
            print("The bot cut you. You Lose.")
        elif a == "Scissors":
            print("Its a TIE!")

    end = input("\nWould you like to play again? (y) / (n) ")
    if end == "n":
        print('Quitting game.')
        break
    elif end == "y":
        continue
    else:
        print('You did not enter a valid letter. Quitting game.')
        break
print("\n")
