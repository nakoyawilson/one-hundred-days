import random
import hangman_words
import hangman_art

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)

# Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

# Create an empty List called display.
display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display.append("_")

# Print blank word before user enters first guess.
print(f"Your word is:\n{' '.join(display)}")

# Use a while loop to let the user guess again.
user_guess = []
while "_" in display:

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess not in user_guess:
        user_guess.append(guess)
    else:
        print(f"You've already guessed {guess}")

    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if guess in chosen_word:
        # Reveal letter
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
                print(f"{' '.join(display)}")
                print(hangman_art.stages[lives])
                if "_" not in display:
                    print("You win!")

    # If guess is not a letter in the chosen_word, reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and program prints "You lose."
    else:
        # Lose a life
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(f"{' '.join(display)}")
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            print(f"You lose.\nThe word was {chosen_word}.")
            break