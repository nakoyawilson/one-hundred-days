alphabet = ["a", "b" ,"c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

text = input("Type your message:\n").lower()
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new_message = ""
    if direction == "encode":
        for char in text:
            if alphabet.index(char) + shift < 26:
                new_index = alphabet.index(char) + shift
                new_char = alphabet[new_index]
                new_message += new_char
            else:
                new_index = alphabet.index(char) + shift - 26
                new_char = alphabet[new_index]
                new_message += new_char
    else:
        for char in text:
            if alphabet.index(char) - shift >= 0:
                new_index = alphabet.index(char) - shift
                new_char = alphabet[new_index]
                new_message += new_char
            else:
                new_index = alphabet.index(char) + 26 - shift
                new_char = alphabet[new_index]
                new_message += new_char
    print(new_message)

encrypt(text,shift)