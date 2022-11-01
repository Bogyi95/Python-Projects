#Rock Paper Scissors Game
import random

options = ["rock", "paper", "scissors"]

computer = options[random.randint(0,2)]

score_player = 0
score_computer = 0

player = ""

while player == "":
    print("************************************")
    print("Choose one:")
    player = input("rock, paper or scissors ?: ")
    print() #makes some space
    

    if player == computer:                                     
        print("%s, it's a tie" %computer)

    elif player == "rock" and computer == "scissors":           
        print("%s, you win" %computer)  
        score_player += 1                      
    elif player == "paper" and computer == "rock":
        print("%s, you win" %computer)
        score_player += 1                     
    elif player == "scissors" and computer == "paper":
        print("%s, you win" %computer)
        score_player += 1   
    elif player != ("rock" or "paper" or "scissors"):       #if there is other word then rock, paper, scissors; break
         print("wrong word")
         break              
    else:
        print("%s, you lose" %computer)
        score_computer += 1

    print() #makes some space
    print("Score: ")
    print("Player: %s" %score_player)
    print("Computer: %s" %score_computer)

    print() #makes some space
    player = ""
    computer = options[random.randint(0,2)]
