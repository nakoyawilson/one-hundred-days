# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Hello. Welcome to the Tip Calculator.")
amount = float(input("What was the final bill amount? $"))
tip = int(input("What percentage would you like to tip (10, 12, or 15)? "))
number_of_persons = int(input("How many people to split the bill?" ))
multiplier = 1 + tip / 100
amount_with_tip = amount * multiplier
each_person_pays = amount_with_tip/number_of_persons
print("Each person should pay: $ {:.2f}".format(each_person_pays))