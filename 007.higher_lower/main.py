# TODO

# Currently we are generating two random numbers which are picking the values from the list.
# But the idea behind it, is that every time You win, you should compare a new value to the old value. Currently I can have two new numbers instead of reusing the old one.


# Imports
import art
import random
import os
from game_data import data

# Global variables

result = 0
continue_game = True


# Functions

def logo():
    print(art.logo)


def vs():
    print(art.vs)


def compare():
    global result
    global continue_game
    global number1
    answer = input("Who has more followers? Type 'A' or 'B': ")

    if answer == "A":
        if data[number1]['follower_count'] >= data[number2]['follower_count']:
            result += 1
            number1 = 0
            print(f"You are right! Current score: {result}.")
        else:
            print(f"Sorry, that's wrong. Final score: {result}.")
            continue_game = False
    elif answer == "B":
        if data[number2]['follower_count'] >= data[number1]['follower_count']:
            result += 1
            number1 = 0
            print(f"You are right! Current score: {result}.")
        else:
            print(f"Sorry, that's wrong. Final score: {result}.")
            continue_game = False


# Print logo

# Generate two random numbers

# How big is the data list?

data_length = len(data)
number1 = random.randint(1, len(data))
number2 = random.randint(1, len(data))


while continue_game:
    os.system('clear')
    logo()

    if number1 == 0:
        number1 = number2
        number2 = random.randint(1, len(data))

    while number1 == number2:
        number2 = random.randint(1, len(data))

    # Print Compare VS Against

    print(f"COMPARE A: {data[number1]['name']}, a {data[number1]['description']}, from {data[number1]['country']}.")
    vs()
    print(f"COMPARE B: {data[number2]['name']}, a {data[number2]['description']}, from {data[number2]['country']}.")
    # Who has more followers? Type 'A' or 'B': 
    compare()
    input("Hit a key to move to another step.")

# Compare function

# Print result
