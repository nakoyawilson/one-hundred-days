from higher_lower_art import logo, vs
from higher_lower_game_data import data
import random
# from replit import clear

# Functions
def choose_first_entries():
    """Chooses two random entries from game data list"""
    choice_a = random.choice(data)
    choice_b = random.choice(data)
    # If choice_b == choice_a, choose again for b
    if choice_b == choice_a:
        choice_b = random.choice(data)
    return choice_a, choice_b

def choose_more_entries(choice_a, choice_b):
    choice_a = choice_b
    choice_b = random.choice(data)
    if choice_b == choice_a:
        choice_b = random.choice(data)
    return choice_a, choice_b

def assign_answer(choice):
    """Assigns player's choice to an answer"""
    if choice == "A":
        answer = choice_a
    elif choice == "B":
        answer = choice_b
    else:
        return "Invalid input"
    return answer

# Compare follower count
def compare_follower_counts(first_choice, second_choice):
    """Compares follower counts and returns correct answer"""
    if first_choice['follower_count'] > second_choice['follower_count']:
        answer = first_choice
    else:
        answer = second_choice
    return answer

def start_round(first_choice, second_choice):
    # Print instructions for player.
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
    print(vs)
    print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")
    # Ask who has more followers
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    return choice

def play_round(choice_a, choice_b):
    player_choice = start_round(choice_a, choice_b)
    correct_answer = compare_follower_counts(choice_a, choice_b)
    player_answer = assign_answer(player_choice)
    return player_choice, correct_answer, player_answer

play_higher_lower = "y"
while play_higher_lower == "y":
    play_higher_lower = input("Do you want to play? Type 'y' or 'n': ").lower()
    if play_higher_lower == "y":
        # # Clear screen
        # clear()
        # Print game logo
        print(logo)
        # Choose two entries from data list: 'A' and 'B'
        choice_a, choice_b = choose_first_entries()
        player_choice, correct_answer, player_answer = play_round(choice_a, choice_b)
        # Display results. If player is correct, add 1 to score.
        # Game continues and B becomes A. Choose new B
        score = 0
        while player_answer == correct_answer:
            # # Clear screen
            # clear()
            # # Print game logo
            # print(logo)
            score += 1
            print(f"You're right! Current score: {score}.")
            choice_a, choice_b = choose_more_entries(choice_a, choice_b)
            player_choice, correct_answer, player_answer = play_round(choice_a, choice_b)
        if player_answer != correct_answer:
            print(f"Sorry, that's wrong. Final score: {score}")
    else:
        print("Thanks for playing!")