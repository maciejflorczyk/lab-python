############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### ToDO #####################

1. Removing cards from the cards.
1. Shuffling cards

### Imports
import art
import random
### Variables
play_game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards  = []
computer_cards = []
user_score = 0
computer_score = 0

def pick_a_card(cards_list, number):
    """ Picking a 'number' of cards from the 'cards' list.
    """
    for number_of_cards in range(0,number):
        cards_list.append(random.choice(cards))



def init_game():
    print(art.logo)

    pick_a_card(my_cards,2)
    pick_a_card(computer_cards,1)

def print_current_result():

    print(f"Your cards: {my_cards}")
    print(f"Sum o your cards: {user_score}")

    print(f"Computer's first cards: {computer_cards}")
    print(f"Sum o computer cards: {computer_score}")

def calculate_score(current_cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(current_cards) == 21 and len(current_cards) == 2:
        return 0
    if 11 in current_cards and sum(current_cards) > 21:
        current_cards.remove(11)
        current_cards.append(1)
    return sum(current_cards)


def final_result():
    print(f"Your final hand: {my_cards} with a sum of {user_score}")
    print(f"Computer final hand: {computer_cards} with a sum of {computer_score}")


def computer_pick():
    while(sum(computer_cards) < 17):
        if random.randint(0,1):
            pick_a_card(computer_cards,1)


def compare_results():
    if user_score > 21 and computer_score > 21:
        print("You went over. You lose 😤")

    if user_score == computer_score:
        print("Draw 🙃")
    elif computer_score == 0:
        print("Lose, opponent has Blackjack 😱")
    elif user_score == 0:
        print("Win with a Blackjack 😎")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score > computer_score:
        print("You win 😃")
    else:
        print("You lose 😤")


while play_game:
    my_cards = []
    computer_cards = []
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if want_to_play == "y":
        play_game = True
        init_game()
        user_score = calculate_score(my_cards)
        computer_score = calculate_score(computer_cards)
        print_current_result()

        while (input("Type 'y' to get another card, type 'n' to pass: ") == "y"):

            pick_a_card(my_cards,1)
            user_score = calculate_score(my_cards)
            computer_score = calculate_score(computer_cards)
            print_current_result()

        ### Computer logic to pick a card ###
        computer_pick()
        #####################################
        user_score = calculate_score(my_cards)
        computer_score = calculate_score(computer_cards)
        final_result()
        compare_results()

    elif want_to_play == "n":
        play_game = False
    else:
        print("Wrong choice")

print("Goodbye!")


#X #print logo
#
#X cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#X print(f"Your cards: {your_cards}")
#X print(f"Computer's first cards: {computer_cards}")
#
# get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
# 
# print(f"Your final hand: {your_cards}")
# print(f"Computer final hand: {computer_cards}")
# 
# print("You win!")
# print("Draw.")
# print("You loose.")
# 
# # karty 1-10
# # walet-krol = 10
# # as 1 lub 11 w zaleznosci co lepsze
# # jezeli dealer ma karty <17 to musi dobrać następną kartę
# 
