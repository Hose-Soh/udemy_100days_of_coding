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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

user_ready = input("Are you ready? y/n: ")

if user_ready == 'n':
    print("You can comeback & play the game anytime later!")

else:
    left_right = input("Which way do you want to go? left/right: ")
    
    if left_right!='left':
        print("Fall into a hole. Game Over.")
    
    else:
        swim_wait = input('''There is a water source in front of you.\nWhat do you want to do? swim/wait: ''')
        
        if swim_wait!='wait':
            print("Attacked by trout. Game Over.")
        
        else:
            door = input('''Suddenly three doors have appeared.\nChoose one. red/blue/yellow: '''
                         )
            if door == 'red':
                print("Burned by fire. Game Over.")
            elif door == 'blue':
                print("Eaten by beasts. Game Over.")
            elif door == 'yellow':
                print("You Win!")
            else:
                print("Game Over.")