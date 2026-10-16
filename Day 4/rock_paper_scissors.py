# Rock Paper Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock Paper Scissors Game")
user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))


if user_choice >= 0 and user_choice <= 2:
    print(rps[user_choice])
else:
    print("Invalid Input, Choose between Rock, Paper and Scissors")
    exit()
print(f"You Choose: {choices[user_choice]}")


computer_choice = random.randint(0, 2)
print(rps[computer_choice])
print(f"Computer Choose: {choices[computer_choice]}")

if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("\nYou Win!")
elif user_choice == computer_choice:
    print("\nIt's a Draw!")
else:
    print("\nYou Lose!")
