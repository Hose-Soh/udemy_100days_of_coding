import random

# assign rock, paper, scissors
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

# make a list of outcomes
outcomes_list = [rock, paper, scissors]

# take input from the user and convert to integer
user_input_index= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

# check if the input from user is valid
if user_input_index >=0 and user_input_index <4:

    # assign user_input to input user chose and randomly chose computers outcome using random.choice
    user_input = outcomes_list[user_input_index]
    computer_input = random.choice(outcomes_list)

    # same output from user and computer means draw
    if user_input==computer_input:
        print(f"You Chose:\n{user_input}\nComputer Chose:\n{computer_input}\nDraw!")
    # users' rock beats computers scissors
    elif user_input==outcomes_list[0] and computer_input==outcomes_list[2]:
        print(f"You Chose:\n{user_input}\nComputer Chose:\n{computer_input}\nYou Won!")
    # users' paper beats computers scissors
    elif user_input==outcomes_list[1] and computer_input==outcomes_list[0]:
        print(f"You Chose:\n{user_input}\nComputer Chose:\n{computer_input}\nYou Won!")
    # users' scissors beat computers paper
    elif user_input==outcomes_list[2] and computer_input==outcomes_list[1]:
        print(f"You Chose:\n{user_input}\nComputer Chose:\n{computer_input}\nYou Won!")
    # all the remaining possibilities where user loses
    else:
        print(f"You Chose:\n{user_input}\nComputer Chose:\n{computer_input}\nYou Lose!")

else:
    # user did not select 0,1,2
    print("Invalid Input")

