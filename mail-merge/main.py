# Create a letter using starting_letter.txt for each name in invited_names.txt
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Create list of names
with open("Input/Names/invited_names.txt") as data:
    names_list = data.readlines()
new_names = []
for name in names_list:
    new_name = name.strip("\n")
    new_names.append(new_name)

# Get letter template
with open("Input/Letters/starting_letter.txt") as template:
    letter_template = template.read()

for name in new_names:
    # Replace the [name] placeholder with the actual name
    new_letter = letter_template.replace("[name]", name)
    # Save the letters in the folder "ReadyToSend"
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
        letter.write(new_letter)

