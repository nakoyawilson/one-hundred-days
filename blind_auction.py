from replit import clear

name = (input("What is your name? "))
bid = float(input("What is your bid? $"))
continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.\n")
auction_result = f"The winner is {name} with a bid of ${bid:.2f}"