import pandas

# Create a dictionary for NATO alphabet:
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
phonetic_code = [nato_dict[letter] for letter in user_input]
print(phonetic_code)

