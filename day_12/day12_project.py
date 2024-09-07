import art, random

EASY_LEVEL = 10
HARD_LEVEL = 5

# function to set the difficulty level
def game_level(level):
    if level=='easy':
        attempts = EASY_LEVEL

    elif level=='hard':
        attempts = HARD_LEVEL
    else:
        print("Wrong Input. Run the Game Again!")
        return 0
    return attempts

# function to check if user got the correct answer within fixed attempts number
def play_game(total_attempts):
    correct_answer = random.choice(range(1, 101))
    # correct_answer = 80
    counter = 0
    while counter < total_attempts:
        print(f"You have {total_attempts-counter} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == correct_answer:
            return print(f"{user_guess} is the correct answer. Well Done!")

        elif user_guess > correct_answer:
            print(f"Higher than the correct answer")
            counter+=1
        elif user_guess < correct_answer:
            print(f"Lower than the correct answer")
            counter+=1
    if counter == total_attempts:
        print("You've used all attempts. You Lose!")

# main function
def main():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Pssst, the correct answer is 2")
    select_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts_counter = game_level(select_level)
    play_game(attempts_counter)

# run main function
main()