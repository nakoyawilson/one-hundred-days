import string
# 1. Create a greeting for your program.
print("Hello! Welcome to the Band Name Generator!")
# 2. Ask the user for the city that they grew up in.
city = input("What is the name of the city that you grew up in?\n")
# 3. Ask the user for the name of a pet.
pet = input("What was the name of your first pet?\n")
# 4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + string.capwords(city) + " " + string.capwords(pet) + ".")
# 5. Make sure the input cursor shows on a new line, see the example at:
#    https://band-name-generator-end.appbrewery.repl.run/
