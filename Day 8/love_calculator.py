# Love Calculator
def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).lower()
    
    true_count = 0
    love_count = 0
    
    for letter in combined_name:
        if letter in ["t","r","u","e"]:
            true_count += 1
        if letter in ["l","o","v","e"]:
            love_count += 1
            
    print(f"{true_count}{love_count}")

calculate_love_score("Kanye West", "Kim Kardashian")
