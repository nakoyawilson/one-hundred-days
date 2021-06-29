from replit import clear

# Ask for name and bid until there are no more bidders
continue_auction = "yes"
auction_bids = {}
while continue_auction == "yes":
  name = (input("What is your name? "))
  bid = float(input("What is your bid? $"))
  continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  auction_bids[name] = bid
  clear()

# Determine highest bid
for bidder in auction_bids:
  winning_bid = 0
  winner = ""
  auction_bid = auction_bids[bidder]
  if auction_bid > winning_bid:
    winning_bid = auction_bid
    winner = bidder

auction_results = f"The winner is {winner} with a bid of ${winning_bid:.2f}"
print(auction_results)