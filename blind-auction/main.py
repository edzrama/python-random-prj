from replit import clear
from art import logo

bidding = {}
continue_bid = True


def add_bidders(first_name, value):
    bidding[first_name] = value


print(logo)
while continue_bid:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    add_bidders(name, bid)
    continue_bid = (input("Are there any other bidders? type 'yes' or 'no'") == "yes")
    clear()

high_val = 0
high_name = ""
for name, val in bidding.items():
    if val > high_val:
        high_val = val
        high_name = name
print(f"the winner is {high_name} with a bid of ${high_val}")
