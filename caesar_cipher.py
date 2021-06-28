from caesar_cipher_art import logo

alphabet = ["a", "b" ,"c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(start_text, cipher_direction, shift_amount):
    # Program continues to work if user enters shift number greater than 26
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    end_text = ""
    if cipher_direction == "encode":
        for char in start_text:
            if alphabet.index(char) + shift_amount < 26:
                new_index = alphabet.index(char) + shift_amount
                new_char = alphabet[new_index]
                end_text += new_char
            else:
                new_index = alphabet.index(char) + shift_amount - 26
                new_char = alphabet[new_index]
                end_text += new_char
    else:
        for char in start_text:
            if alphabet.index(char) - shift_amount >= 0:
                new_index = alphabet.index(char) - shift_amount
                new_char = alphabet[new_index]
                end_text += new_char
            else:
                new_index = alphabet.index(char) + 26 - shift_amount
                new_char = alphabet[new_index]
                end_text += new_char
    print(f"The {cipher_direction}d text is {end_text}")

# Import and print logo from caesar_cipher_Art.py when the program starts
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(start_text=text, cipher_direction=direction,shift_amount=shift)