# The Secret Auction
import os

from art import logo

print(logo)
print("Welcome to the secret auction program.\n")

bids = {}
should_continue = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_value = bidding_record[bidder]

        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while should_continue:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    more_bidders = input("\nAre ther any other bidders? Type 'yes' or 'no'.\n").lower()

    if more_bidders == "yes":
        os.system("clear")
    elif more_bidders == "no":
        should_continue = False
        find_highest_bidder(bids)
