import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)

display = ['_']*len(chosen_word)

while chosen_word !=''.join(display):
    guess = input("Guess a letter: ").lower()

    for idx, letter in enumerate(chosen_word):

        if letter == guess:
            display[idx]= letter

    print(''.join(display))

print("You have won the game!")
