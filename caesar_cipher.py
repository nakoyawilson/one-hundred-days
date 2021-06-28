alphabet = ["a", "b" ,"c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

text = input("Type your message:\n").lower()
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for char in plain_text:
        if alphabet.index(char) + shift_amount < 26:
            new_index = alphabet.index(char) + shift_amount
            new_char = alphabet[new_index]
            cipher_text += new_char
        else:
            new_index = alphabet.index(char) + shift_amount - 26
            new_char = alphabet[new_index]
            cipher_text += new_char
    print(cipher_text)

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for char in cipher_text:
        if alphabet.index(char) - shift >= 0:
            new_index = alphabet.index(char) - shift_amount
            new_char = alphabet[new_index]
            plain_text += new_char
        else:
            new_index = alphabet.index(char) + 26 - shift_amount
            new_char = alphabet[new_index]
            plain_text += new_char
    print(plain_text)

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(cipher_text=text, shift_amount=shift)