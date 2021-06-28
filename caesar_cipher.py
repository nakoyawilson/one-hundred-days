from caesar_cipher_art import logo

alphabet = ["a", "b" ,"c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(start_text, cipher_direction, shift_amount):
    # Program continues to work if user enters shift number greater than 26
    shift_amount = shift_amount % 26
    end_text = ""
    for char in start_text:
        # Keep chracters that are not in alphabet
        if char not in alphabet:
            end_text += char
        elif cipher_direction == "encode":
            if alphabet.index(char) + shift_amount < 26:
                new_index = alphabet.index(char) + shift_amount
                new_char = alphabet[new_index]
                end_text += new_char
            else:
                new_index = alphabet.index(char) + shift_amount - 26
                new_char = alphabet[new_index]
                end_text += new_char
        else:
            if alphabet.index(char) - shift_amount >= 0:
                new_index = alphabet.index(char) - shift_amount
                new_char = alphabet[new_index]
                end_text += new_char
            else:
                new_index = alphabet.index(char) + 26 - shift_amount
                new_char = alphabet[new_index]
                end_text += new_char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and print logo from caesar_cipher_Art.py when the program starts
print(logo)

# Ask user if they want to restart program
continue_program = "yes"
while continue_program == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, cipher_direction=direction,shift_amount=shift)
    continue_program = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()