import random

options = ["rock", "paper", "scissors"]

computer = options[random.randint(0,2)]

player = ""

while player == "":
    print("Choose one")
    player = input("rock, paper or scissors ?: ")
    if player == computer:                                     
        print("%s, it's a tie" %computer)

    elif player == "rock" and computer == "scissors":           
        print("%s, you win" %computer)                        
    elif player == "paper" and computer == "rock":
        print("%s, you win" %computer)                     
    elif player == "scissors" and computer == "paper":
        print("%s, you win " %computer)                     
    else: print("%s, you lose" %computer) 
     
    player = ""
    computer = options[random.randint(0,2)]
