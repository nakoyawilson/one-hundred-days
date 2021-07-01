import random

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
    player_cards = []
    computer_cards = []
    # Deal user a starting hand of 2 random card values
    for card in range(2):
        deal_card = random.choice(cards)
        player_cards.append(deal_card)
    print(player_cards)
    # Deal computer a starting hand of 2 random card values
    for card in range(2):
        deal_card = random.choice(cards)
        computer_cards.append(deal_card)
    print(computer_cards)

play_blackjack = True
while play_blackjack:
    start_game = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")
    if start_game == "yes":
        blackjack()
    else:
        play_blackjack = False
        print("Thanks for playing!")