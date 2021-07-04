from higher_lower_art import logo, vs
from higher_lower_game_data import data
import random

# Print game logo
print(logo)

# Choose two entries from data list: 'A' and 'B'
choice_a = random.choice(data)
choice_b = random.choice(data)
if choice_b == choice_a:
    choice_b = random.choice(data)

# Print instructions for player.
print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
print(vs)
print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")

# Ask who has more followers
player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
player_answer = ""
if player_choice == "A":
    player_answer = choice_a
elif player_choice == "B":
    player_answer = choice_b
else:
    print("Invalid input")
print(player_answer)

# Compare follower count
correct_answer = ""
if choice_a['follower_count'] > choice_b['follower_count']:
    correct_answer = choice_a
else:
    correct_answer = choice_b
print(correct_answer)

# Display results

# If player is correct, add 1 to score
# Game continues and B becomes A
# Choose new B

# If player is wrong, game ends