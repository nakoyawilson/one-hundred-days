letters = ["a", "b" ,"c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

message = input("Type message here: ")
method = input("Would you like to encode or decode? ")
key = int(input("What is the key? "))

new_message = ""
if method == "encode":
    for char in message:
        if letters.index(char) + key < 26:
            new_index = letters.index(char) + key
            new_char = letters[new_index]
            new_message += new_char
        else:
            new_index = letters.index(char) + key - 26
            new_char = letters[new_index]
            new_message += new_char
else:
    for char in message:
        if letters.index(char) - key >= 0:
            new_index = letters.index(char) - key
            new_char = letters[new_index]
            new_message += new_char
        else:
            new_index = letters.index(char) + 26 -key
            new_char = letters[new_index]
            new_message += new_char
print(new_message)