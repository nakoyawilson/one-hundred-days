from morse_code import morse_code_dictionary

rules = """
Individual letters are separated by a forward slash (/) and individual words are separated by a DOUBLE forward slash (//).
Sentences in this format are separated by Four slashes (////)."""

text_to_translate = input("Input sentence to translate: ")
string_minus_last_character = text_to_translate[:-1]
last_character = text_to_translate[-1]
morse_code_translation = ""
for character in string_minus_last_character:
    if character == " " or character == ".":
        morse_code_translation += morse_code_dictionary[character]
    else:
        morse_code = morse_code_dictionary[character.upper()]
        morse_code_translation += f"{morse_code}/"

complete_translation = morse_code_translation + morse_code_dictionary[last_character.upper()]
results = f"Your text as morse code is:\n\n{complete_translation}"
print(results)