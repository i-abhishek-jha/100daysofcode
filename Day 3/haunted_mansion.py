# Haunted Mansion
print(r'''
                                              ,           ^'^  _
                                              )               (_) ^'^
         _/\_                    .---------. ((        ^'^
         (('>                    )`'`'`'`'`( ||                 ^'^
    _    /^|                    /`'`'`'`'`'`\||           ^'^
    =>--/__|m---               /`'`'`'`'`'`'`\|
         ^^           ,,,,,,, /`'`'`'`'`'`'`'`\      ,
                     .-------.`|`````````````|`  .   )
                    / .^. .^. \|  ,^^, ,^^,  |  / \ ((
                   /  |_| |_|  \  |__| |__|  | /,-,\||
                  /_____________\ |")| |  |  |/ |_| \|
                   |  __   __  |  '==' '=='  /_______\    
                   | /  \ /  \ |   _______   |,^, ,^,|   
                   | |--| |--| |  ((--.--))  ||_| |_||  
     _      _      | |__| |("| |  ||  |  ||  |,-, ,-,|   
   ,' ',  ,' ',    |           |  ||  |  ||  ||_| |_||   
.,,|RIP|,.|RIP|,.,,'==========='==''=='==''=='=======',,....,,,,.,
''')
print("Welcome to the Haunted Mansion!")
print("Your mission is to escape before midnight.")
print("You enter the mansion, and the front door slams shut!")
print("You hear a strange voice whisper:")
print("You may leave before midnight... if you survive.")

has_key = False
choice1 = input("Do you want to go upstairs or enter the basement? Type \"upstairs\" or \"basement\"\n").lower()
if choice1 == "basement":
    print("You enter the basement and find a locked chest.")
    choice2 = input("Do you want to search for a key or force the chest open? Type \"force\" or \"search\"\n").lower()
    if choice2 == "search":
        print("You find a silver key inside an old drawer!")
        has_key = True
    elif choice2 == "force":
        print("You trigger a trap! Game Over!")
        exit()

    else:
        print("Invalid choice! Game Over!")
        exit()

elif choice1 == "upstairs":
    print("A ghost appears in front of you!")

    choice3 = input("Do you want to hide in a room or run down the hallway? Type \"hide\" or \"run\"\n").lower()
    if choice3 == "hide":
        print("You hide in a room and discover a silver key!")
        has_key = True
    elif choice3 == 'run':
        print("The ghost catches you. Game Over!")
        exit()
    else:
        print("Invalid choice! Game Over!")
        exit()

else:
    print("Invalid choice! You must choose upstairs or basement.")
    print("Game Over!")
    exit()

if has_key:
    print("\nYou reach the final hallway."
          "You see three possible escape routes.")

    choice4 = input("Where do you want to go? Type \"door\", \"window\", or \"tunnel\":\n").lower()

    if choice4 == "door":
        print("\nYou insert the silver key into the lock."
              "The door creaks open."
              "Congratulations! You escaped the Haunted Mansion!")

    elif choice4 == "window":
        print("\nYou climb through the window."
              "You land outside from 9th story building")
        print("You are dead. Game Over!")

    elif choice4 == "tunnel":
        print("\nYou enter a dark, secret tunnel."
              "At the end, you discover a mysterious crystal."
              "The crystal reveals the mansion's hidden treasure!"
              "Secret Ending! You discovered the hidden treasure.")

    else:
        print("\nYou hesitate for too long."
              "Midnight strikes. Game Over!")
