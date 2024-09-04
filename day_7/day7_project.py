# import packages and other files
import random
import hangman_words, hangman_art

# assign lives to 6, stages to stages list from hangman_art file, print logo from hangman_art file
lives = 6
stages = hangman_art.stages
print(hangman_art.logo)

# randomly choose a word from word_list in hangman_words file
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

# create a placeholder for the chosen word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# assign game_over to bool False
game_over = False
correct_letters = []

# run while loop until game_over is True
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    
    # take input from user and convert that input to lowercase string 
    guess = input("Guess a letter: ").lower()

    # create empty list
    display = ""
    
    # condition to check if the guess is in the chosen_word. if not then decrease lives 
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives-=1
    # condition to check if the character is already guessed before
    elif guess in correct_letters:
        print(f"You've already guessed {guess}")
    
    # run for loop to search if user input matches any character from the chosen word or already guessed 
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:

            display += letter
        else:
            display += "_"


    print("Word to guess: " + display)

    # if all lives lost then game over
    if lives == 0:
        game_over = True

        print(f"***********************IT WAS '{chosen_word}' YOU LOSE**********************")
    # if there 
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(stages[lives])