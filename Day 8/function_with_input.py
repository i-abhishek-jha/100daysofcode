# Functions with inputs

# Simple Function that packages code into a named block
def greet():
    print("Hi, Abhi.")
    print("Good day! Abhi")

greet()


# Function that allows for inputs
def greet_with_name(name):
    print(f"Hi, {name}.")
    print(f"Good day! {name}")

user = input("What's you're name!\n")
greet_with_name(user)