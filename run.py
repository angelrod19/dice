# Developed on December 8th, 2017
# by Angel Rodriguez
# Last modified on: December 8th, 2017

import time
import random

def roll(): # defines a function to create and print a # from 1 to 6
    number = random.randint(1,6)
    print("Your number is {0}".format(number))

print("Hello! This is a simple program that will roll a dice.")
time.sleep(1.5)
roll()

loop = True # LCV

while (loop == True):
    decision = str(input("\nDo you want to roll again? (y / n): "))

    # if yes, roll() functions gets called. if not, program is terminated

    if (decision == "n" or decision == "N" or decision == "no"):
        print("Thanks for playing!")
        loop = False
        exit()
    elif (decision == "y" or decision == "Y" or decision == "yes"):
        roll()
    else:
        print("Invalid input. Exiting program.")
        loop = False
        exit()
