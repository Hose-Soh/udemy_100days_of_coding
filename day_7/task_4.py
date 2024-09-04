import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

correct_letters = []
lives = 6

while lives>0:
    guess = input("Guess a letter: ").lower()

    display = ""

    if guess not in chosen_word:
        lives = lives-1
    for letter in chosen_word:
        print("for loop")
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            # print("if statement")
            # print(display)
        elif letter in correct_letters:
            display += letter
            # print("elif statement")
            # print(display)
        else:
            display += "_"
            # print("else statement")
            # print(display)

    print(display)
    print(stages[lives])
    
    if lives == 0:
        print("You lose!")
    if "_" not in display:
        game_over = True
        print("You win.")