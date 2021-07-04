from higher_lower_art import logo, vs
from higher_lower_game_data import data
import random

# Functions
def choose_entry():
    """Chooses random entry from game data list"""
    return random.choice(data)

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

def play_game(first_choice, second_choice):
    # Print instructions for player.
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
    print(vs)
    print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")
    # Ask who has more followers
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    return choice

# Print game logo
print(logo)

play_higher_lower = "y"
while play_higher_lower == "y":
    play_higher_lower = input("Do you want to play? Type 'y' or 'n': ").lower()
    if play_higher_lower == "y":
        # Choose two entries from data list: 'A' and 'B'
        choice_a = choose_entry()
        choice_b = choose_entry()
        if choice_b == choice_a:
            choice_b = choose_entry()
        player_choice = play_game(choice_a, choice_b)
        correct_answer = compare_follower_counts(choice_a, choice_b)
        player_answer = assign_answer(player_choice)
        # Display results. If player is correct, add 1 to score.
        # Game continues and B becomes A. Choose new B
        score = 0
        if player_answer == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}.")
            while player_answer == correct_answer:
                choice_a = choice_b
                choice_b = choose_entry()
                if choice_b == choice_a:
                    choice_b = choose_entry()
                player_choice = play_game(choice_a, choice_b)
                correct_answer = compare_follower_counts(choice_a, choice_b)
                player_answer = assign_answer(player_choice)
        # If player is wrong, game ends
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    else:
        print("Thanks for playing!")