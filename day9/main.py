from art import logo
# from replit import clear

print(logo)
print("Welcome to the secret auction program.")
bids = {}

def add_bidder(name, bid):
    bids[name] = bid

def find_highest_bidder(bids):

    higgest_bid = 0
    winner = ""

    for bidder_name in bids:
        if bids[bidder_name] > higgest_bid:
            higgest_bid = bids[bidder_name]
            winner = bidder_name

    print(f"The winner is {winner} with a bid of ${higgest_bid}")

new_bidder = True

while new_bidder:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    add_bidder(name, bid)
    action = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    # clear()
    if action == "no" or action == "n":
        new_bidder = False
        print("The auction is done!\n\n")
        find_highest_bidder(bids)