# Direct Aproach
import art
print(art.logo)

blind_auction = {}
new_bids = True
winner_bid = 0
winner = ""
while new_bids:
    name = str(input("What's your name: \n"))
    price = float(input("Your bid amount: \n"))
    blind_auction[name] = price
    more_bids = input("You other person wants' to bid: \'y\' for yes and \'n\' for no: \n").lower()

    if more_bids == "y":
        print("\n" * 100)
    elif more_bids == "n":
        new_bids = False
        for key in blind_auction:
            value = blind_auction[key]
            if winner_bid < value:
                winner_bid = value
                winner = key


print(f"The winner is : {winner} with bid of ${winner_bid}" )






