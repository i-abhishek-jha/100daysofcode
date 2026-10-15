# RollerCoaster
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
amount = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age >= 18:
        amount = 12
        print("Adult tickets are $12.")
    elif age < 12:
        amount = 5
        print("Child tickets are $5.")
    elif age >= 45 and age <= 55:
        print("Ride is free for you with the Free Photo")
        bill = -3    
    else:
        amount = 7
        print("Youth tickets are $7.")

    photo = input("Do you want your Picture 'n' for No and 'y' for Yes? ").lower()
    if photo == "y":
        amount = amount + 3

    print(f"You have to pay ${amount}")

else:
    print("Sorry you have to grow taller before you can ride.")

