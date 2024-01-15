### Imports ###
import random
import art
### Global variables ###
play_the_game = True
EASY_DIFFICULTY_TURNS = 10
HARD_DIFFICULTY_TURNS = 5

### FUNCITONS ###
def play():
    welcome()
    difficulty = choose_difficulty()
    number_of_games = f_number_of_games(difficulty)
    computer_number = computer_pick()

    while number_of_games:
        print(f"You have {number_of_games} attempts remaining to guess the number.")
        guessed_number = guess()
        result = compare(guessed_number, computer_number)
        number_of_games -= 1

        if result == 1:
            print("Too high!")
            print("Guess again!")
        elif result == 2:
            print("Too low!")
            print("Guess again!")
        elif result == 0:
            print(f"You got it! The answer was {computer_number}.")
            return

def welcome():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking off a number between 1 and 100.")

def choose_difficulty():
    difficulty = input("Choose a diffficulty. Type 'easy' or 'hard': ")
    return difficulty

def f_number_of_games(choice):
    if choice == "easy":
        number_of_games = EASY_DIFFICULTY_TURNS
        return number_of_games
    elif choice == "hard":
        number_of_games = HARD_DIFFICULTY_TURNS = 10
        return number_of_games

def guess():
    guessed_number = int(input("Make a guess: "))
    return guessed_number

def computer_pick():
    computer_number = random.randint(1,100)
    return computer_number

def compare(my_number, computer_number):
    if my_number > computer_number:
        return 1
    elif my_number < computer_number:
        return 2
    elif my_number == computer_number:
        return 0

### PROGRAM ###
while play_the_game:
    if input("Do you want to play the game? y or n? ") == "y":
        play()
    else:
        play_the_game = False
