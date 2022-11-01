# Guess the number game 

import random

print("Hello")
print("Let's play a game")
print("I'll pick a number and you gonna guess it")
print("I'm gonna pick a number between 1 and 100 and you need to guess it")
print("Let's start")

random_number = int(random.randint(1,100))  #computer picks random number

print("Pick a number(I'm gonna tell you if it's lower or higher than mine)")

guess = input("Pick a number between 1 and 100: ")

while int(guess) != random_number:
    if int(guess) > random_number:
        print("Too high")
        guess = input("Pick another: ")
    if int(guess) < random_number:
        print("Too low")
        guess = input("Pick another: ")
    else:
        print("You won that's my number")

