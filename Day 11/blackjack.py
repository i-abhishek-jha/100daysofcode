# Blackjack Game
import random

def draw_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


computer_cards = []

computer_cards.append(draw_cards())
computer_cards.append(draw_cards())
print(computer_cards)

user_cards = []

user_cards.append(draw_cards())
print(user_cards)

def card_sum():
    return sum(computer_cards), sum(user_cards)

computer_sum, user_sum  = card_sum()
print(f"Computer Sum: , {computer_sum}")
print(f"User Sum: {user_sum}")



