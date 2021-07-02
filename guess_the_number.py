# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
#from replit import clear
import guess_the_number_art

# Create function for guess the number game
def guess_the_number(difficulty_mode):
    number = random.randint(num1, num2)
    num_of_tries = difficulty_mode
    while num_of_tries > 0:
        print(f"You have {num_of_tries} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        num_of_tries -= 1
        if user_guess == number:
            print(f"You got it! The answer was {number}!")
            break
        elif num_of_tries == 0:
            print(f"Sorry. You've run out of guesses. The number I was thinking of was {number}")
        elif user_guess > number:
            print("Too high.")
        else:
            print("Too low.")

# Ask player if they want to play, call guess_the_number function if yes
num1 = 1
num2 = 100
print(guess_the_number_art.logo)
print(f"Welcome to the Number Guessing Game!")
start_game = "y"
while start_game == "y":
    start_game = input("Do you want to play? Type 'y' or 'n': ").lower()
    if start_game == "y":
        # clear()
        print(f"I'm thinking of a number between {num1} and {num2}")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        while difficulty not in ["easy", "hard"]:
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            tries = 10
        else:
            tries = 5
        guess_the_number(tries)
    else:
        print("Thanks for playing!")