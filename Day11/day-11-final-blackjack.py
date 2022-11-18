########## Blackjack Project ##################
########## Our Blackjack House Rules ##########

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import os

from art import logo

def deal_card():
    """
    Returns a random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)

    return random_card

def calculate_score(cards_list):
    """
    Take a list of cards and return the score calculated form the cards.
    """
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)

    return sum(cards_list)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Computer wins!!!"

    if user_score == computer_score:
        return "It's a draw!"
    elif user_score == 0 or computer_score > 21:
        return "User wins!!!"
    elif computer_score == 0 or user_score > 21:
        return "Computer wins!!!"
    elif user_score > computer_score:
        return "User wins!!!"
    else:
        return "Computer wins!!!"

def play_blackjack():
    print(logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while is_game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            get_new_card = input("Type 'y' to get another card or type 'n' to pass: ").lower()

            if get_new_card == "y":
                user_cards.append(deal_card())
                # user_score = calculate_score(user_cards)
            elif get_new_card == "n":
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system("clear")
  play_blackjack()
