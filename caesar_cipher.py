alphabet = ["a", "b" ,"c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

text = input("Type your message:\n").lower()
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
shift = int(input("Type the shift number:\n"))

def caesar(start_text, cipher_direction, shift_amount):
    new_text = ""
    if cipher_direction == "encode":
        for char in start_text:
            if alphabet.index(char) + shift_amount < 26:
                new_index = alphabet.index(char) + shift_amount
                new_char = alphabet[new_index]
                new_text += new_char
            else:
                new_index = alphabet.index(char) + shift_amount - 26
                new_char = alphabet[new_index]
                new_text += new_char
    else:
        for char in start_text:
            if alphabet.index(char) - shift_amount >= 0:
                new_index = alphabet.index(char) - shift_amount
                new_char = alphabet[new_index]
                new_text += new_char
            else:
                new_index = alphabet.index(char) + 26 - shift_amount
                new_char = alphabet[new_index]
                new_text += new_char
    print(new_text)

caesar(start_text=text, cipher_direction=direction,shift_amount=shift)