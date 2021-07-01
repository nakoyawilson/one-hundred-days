import random
from blackjack_art import logo

# Our Blackjack House Rules:
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    """Creates a game of Blackjack"""
    # Print logo
    print(logo)
    player_cards = []
    computer_cards = []
    player_score = 0
    computer_score = 0
    # Deal user a starting hand of 2 random card values
    for card in range(2):
        deal_card = random.choice(cards)
        player_cards.append(deal_card)
    # Deal computer a starting hand of 2 random card values
    for card in range(2):
        deal_card = random.choice(cards)
        computer_cards.append(deal_card)
    # Calculate the user's score based on card values
    player_score = sum(player_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if computer_score == 21:
        print("You lose.")
    elif player_score == 21:
        print("Blackjack! You win.")
    elif player_score > computer_score:
        print("You win!")
    elif player_score == computer_score:
        print("It's a draw")
    another_card = True
    while another_card:
        # Ask the user if they want to get another card
        continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
        if continue_game == 'y':
            deal_card = random.choice(cards)
            player_cards.append(deal_card)
            player_score = sum(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")
        else:
            another_card = False
            computer_score = sum(computer_cards)
            while computer_score < 17:
                deal_card = random.choice(cards)
                computer_cards.append(deal_card)
                computer_score = sum(computer_cards)
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

play_blackjack = True
while play_blackjack:
    start_game = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")
    if start_game == "yes":
        blackjack()
        # clear()
    else:
        play_blackjack = False
        print("Thanks for playing!")