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
print("Welcome to Treasure Island!")
print("You arrive on an island with a mission to find the treasure.")
print("Unfortunately, you are not given a map so you must use your intuition to find it.")
print("You proceed along the dirt path until you get to a fork in the road.")
print("You can either go right and head towards the forest or left and head towards the river.")
direction = input("Which way do you go (left or right)? ").lower()
if direction == "left":
    print("You choose to go left and head towards the river.")
    print("From the river bank you can see a cabin on the other side.")
    print("You estimate the river is 100 meters wide.")
    print("There's a sign that says the boat to cross arrives at the top of every hour.")
    print("You can either swim across to the other side of the river or wait for the next boat.")
    transport = input("What do you do (swim or wait)? ").lower()
    if transport == "wait":
        print("You decide to wait for the boat.")
        print("At the top of the hour it arrives and you make it safely to the other side.")
        print("You enter the cabin and find yourself in a hallway with three closed doors.")
        print("To your left is a blue door. To your right is a yellow door. Straight ahead is a red door.")
        color = input("Which door do you go through (red, yellow or blue)? ").lower()
        if color == "yellow":
            print("You open the yellow door and find a treasure chest. You win!")
        elif color == "red":
            print("You open the red door and you're immediately engufled in flames. Game Over.")
        elif color == "blue":
            print("You open the blue door and you're attacked by beasts. Game Over.")
        else:
            print("You don't choose a door and instead decide to leave. Game Over.")
    elif transport == "swim":
        print("You're eager to get across the river so you opt to swim.")
        print("You swim about halfway to the other side when you're attacked by trout. Game Over.")
    else:
        print("You decide you don't actually want to find the treasure. Game Over.")
elif direction == "right":
    print("You choose to go right and head towards the forest.")
    print("As you approach the forest it becomes harder and harder to see.")
    print("You fall into a hole. Game Over.")
else:
    print("You decide you don't actually want to find the treasure. Game Over.")