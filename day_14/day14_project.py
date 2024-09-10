import game_data, art
import random


def main():
    score = 0
    compare_a = random.choice(game_data.data)
    compare_b = random.choice(game_data.data)

    while True:
        while compare_a==compare_b:
            compare_b = random.choice(game_data.data)
            
        print(art.logo)
        print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}.")
        print(art.vs)
        print(f"Against B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}.")

        user_select = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_select=='a' and compare_a['follower_count'] > compare_b['follower_count']:
            score+=1
            print(f"You're right! Current score {score}")
            print("\n"*20)
            compare_b = random.choice(game_data.data)

        elif user_select=='b' and compare_a['follower_count'] < compare_b['follower_count']:
            score+=1
            print(f"You're right! Current score {score}")
            print("\n" * 20)
            compare_a = compare_b
            compare_b = random.choice(game_data.data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break

main()