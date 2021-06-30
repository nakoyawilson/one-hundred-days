from replit import clear
from blind_auction_art import logo

# Determine highest bid
def find_winning_bid(auction_dictionary):
  winning_bid = 0
  winner = ""
  for bidder in auction_dictionary:
    auction_bid = auction_dictionary[bidder]
    if auction_bid > winning_bid:
      winning_bid = auction_bid
      winner = bidder
  results = f"The winner is {winner} with a bid of ${winning_bid:.2f}"
  print(results)

# Print logo
print(logo)

# Ask for name and bid until there are no more bidders
continue_auction = "yes"
auction_bids = {}
while continue_auction == "yes":
  name = (input("What is your name? "))
  bid = float(input("What is your bid? $"))
  continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  auction_bids[name] = bid
  clear()
find_winning_bid(auction_bids)