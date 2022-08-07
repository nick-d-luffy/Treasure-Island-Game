print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Where do you want to go? Left or Right\n ").lower()

if direction == "left":
    choice_1 = input(
        "You have come across a lake. Do you want to Swim or Wait?\n ").lower(
        )
    if choice_1 == "wait":
        choice_2 = input(
            "You have made it to a house. Choose a door. Red, Yellow or Blue\n "
        ).lower()
        if choice_2 == "red":
            print("You got incinerated by a dragon!\nGame Over!")
        elif choice_2 == "yellow":
            print("You win!\nWinner Winner Chicken Dinner")
        elif choice_2 == "blue":
            print("You get killed by a madman/Game Over!")
        else:
            print("The door doesnt exist/nGame Over!")
    else:
        print("You got eaten by a Crocodile!\nGame Over!")
else:
    print("You got hit by a rock!\nGame Over!")

