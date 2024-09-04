import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = str.lower(input("Guess a letter: "))

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
