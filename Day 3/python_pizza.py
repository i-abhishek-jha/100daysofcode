# Python Pizza
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

amount = 0


if size == "s":
    amount += 15
elif size == "m":
    amount += 20
elif size == "l":
    amount += 25
else:
    print("You have chosen an invalid size.")
    exit()

if pepperoni == "y":
    if size == "s":
        amount += 2
    else:
        amount += 3

if extra_cheese == "y":
    amount += 1

print(f"Your final bill is: ${amount}.")