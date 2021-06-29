from replit import clear

continue_auction = "yes"
auction_bids = {}
while continue_auction == "yes":
  name = (input("What is your name? "))
  bid = float(input("What is your bid? $"))
  continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  auction_bids[name] = bid
  clear()

auction_result = f"The winner is {name} with a bid of ${bid:.2f}"