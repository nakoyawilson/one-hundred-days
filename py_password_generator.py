import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for letter in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    password += random_letter
for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password += random_symbol
for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password += random_number

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_characters = []
for character in password:
    password_characters.append(character)
random.shuffle(password_characters)
randomised_password = ""
for character in password_characters:
    randomised_password += character
print(f"Your password is: {randomised_password}")

# Copy password to clipboard
copy_to_clipboard = input("Would you like to copy your password to the clipboard? Type 'y' or 'n':\n")
if copy_to_clipboard == "y":
    pyperclip.copy(randomised_password)