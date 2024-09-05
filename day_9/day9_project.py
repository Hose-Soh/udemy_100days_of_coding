import art

print(art.logo)

name_bid = {}

while True:
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    name_bid[user_name] = user_bid

    restart = input("Are there any other bidder? Type 'yes' or 'no': ")
    if restart == 'no':
        break
    print("*"*50)
highes_bid = list(name_bid.values())[0]
winner = ''
# print(highes_bid)

for name, bid in name_bid.items():
    if bid>highes_bid:
        highes_bid=bid
        winner=name

print(f"The winner is {winner} with a bid of ${highes_bid}")
