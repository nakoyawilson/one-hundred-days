import random
import hangman_words

#Step 5

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

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

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)

# Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

# Create an empty List called display.
display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display.append("_")

# Use a while loop to let the user guess again.
while "_" in display:

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

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

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    else:
        # Lose a life
        print(f"{' '.join(display)}")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("You lose.")
            break

#TODO-2: - Import the stages from hangman_art.py and make this error go away.