import random

#Step 3

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display.
display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display.append("_")

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

if guess in chosen_word:
    # Reveal letter
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess
else:
    # Lose a life
    pass

# Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)