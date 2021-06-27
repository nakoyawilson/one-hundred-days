import random

#Step 4

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

# Create an empty List called display.
display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display.append("_")

# Use a while loop to let the user guess again.
while "_" in display:

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    if guess in chosen_word:
        # Reveal letter
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
                print(f"{' '.join(display)}")
                print(stages[lives])
                if "_" not in display:
                    print("You win!")

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    else:
        # Lose a life
        # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
        print(f"{' '.join(display)}")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("You lose.")
            break

    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
