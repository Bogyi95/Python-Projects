# Guess the number game 

import random

print("Hello")
print("Let's play a game")
print("I'll pick a number and you gonna guess it")
print("I'm gonna pick a number between 1 and 100 and you need to guess it")
print("Let's start")

random_number = int(random.randint(1,100))                                      #computer picks random number

print("Pick a number(I'm gonna tell you if it's lower or higher than mine)")

guess = input("Pick a number between 1 and 100: ")

attempts = 0

while int(guess) < 1 or int(guess) > 100:
    print("Ty durniu you picked a number outside of the range")
    guess = input("Pick again: ")
    

while int(guess) != random_number:                                              #while the numbers are different do:
    if int(guess) > random_number:                                              #if the guessed number is higher
        print("Too high")
        guess = input("Pick another: ")
        attempts += 1
    if int(guess) < random_number:                                              #if the guessed number is lower
        print("Too low")
        guess = input("Pick another: ")
        attempts += 1
else:                                                                           #else if the numbers are equal ; cuz ther is no other option
    attempts += 1                                                                       
    if attempts == 1:
        print("WOW that's my number. You guessed it in first try!")
    else:                                      
        print("You won that's my number")
        print("You guessed my number in: %s attempts" %attempts)
