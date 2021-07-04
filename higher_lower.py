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
print(choice_a)
print(choice_b)

# Print instructions to player.

# Ask who has more followers

# Display results

# If player is correct, add 1 to score
# Game continues and B becomes A
# Choose new B

# If player is wrong, game ends