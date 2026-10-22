# Life in Weeks
def life_in_weeks(current_age):
    left_years = 90 - current_age
    left_weeks = left_years * 365 // 7

    print(f"You have {left_weeks} weeks left.")

current_age = int(input("What's your age?\n"))
life_in_weeks(current_age)