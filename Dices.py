#Simple Dices Simulator
import random

min_value = 1
max_value = 6

roll = "y"

while roll == "y":

    print("Rolling the dice")
    print("You rolled :")
    print(random.randint(min_value, max_value))
    print("and")
    print(random.randint(min_value, max_value))
    print("Do you want to roll again?")

    roll = input("Type y to continue(anything other than y will close program) : ")