import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_draw(exist_card):
    """
    :param exist_card: list of cards drawn
    :return: return card number depending on the drawn card
    """
    # randomly draw card
    new_card = random.choice(cards)
    # if the total sum of cards after drawing an '11' is more than 21 then replace
    # the new card with 1
    if new_card==11 and new_card+sum(exist_card) > 21:
        return 1
    else:
        return new_card


while True:

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'n':
        break

    print(art.logo)
    user_card = []
    comp_card = []
    user_card = [card_draw(user_card), card_draw(user_card)]
    comp_card = [card_draw(comp_card), card_draw(comp_card)]

    # check if the player or dealer got blackjack in first two cards
    if sum(comp_card) == 21:
        print(f"Your cards: {user_card}, current score: {sum(user_card)}")
        print(f"Computer's first card: {comp_card[0]}")
        print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
        print(f"Computer's final hand: {comp_card}, final score: {sum(comp_card)}")
        print("Computer had Blackjack. Lose!")
        print("\n" * 5)
        continue
    elif sum(user_card) == 21:
        print(f"Your cards: {user_card}, current score: {sum(user_card)}")
        print(f"Computer's first card: {comp_card[0]}")
        print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
        print(f"Computer's final hand: {comp_card}, final score: {sum(comp_card)}")
        print("Win with a Blackjack 😎")
        print("\n"*5)
        continue

    while True:
        print(f"Your cards: {user_card}, current score: {sum(user_card)}")
        print(f"Computer's first card: {comp_card[0]}")

        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card=='n':
            # dealer draw cards until the sum is more than 16
            while sum(comp_card)<17:
                comp_card.append(card_draw(comp_card))
                # check if the value is over 21, if it is the show result and skip the other codes
                if sum(comp_card) > 21:
                    print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
                    print(f"Computer's final hand: {comp_card}, final score: {sum(comp_card)}")
                    print("Opponent went over. You win 😁")
                    print("\n" * 5)
                    break
            break
        else:
            # user draw card until sum is over 21 or user choose to not draw card anymore
            user_card.append(card_draw(user_card))
            if sum(user_card) > 21:
                print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
                print(f"Computer's final hand: {comp_card}, final score: {sum(comp_card)}")
                print("You went over. You lose 😭")
                print("\n" * 5)
            continue


    # check other conditions if the values of user and computer are not over 21
    if sum(user_card) <=21 and sum(comp_card)<=21:
        if sum(user_card) == sum(comp_card):

            print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
            print(f"Computer's final hand: {comp_card}, final score: {sum(comp_card)}")
            print("Draw")
            print("\n" * 5)

        elif sum(user_card) > sum(comp_card):
            print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
            print(f"Computer's final hand: {comp_card}, final score: {sum(comp_card)}")
            print("You win 😁")
            print("\n" * 5)

        else:
            print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
            print(f"Computer's final hand: {comp_card}, final score: {sum(comp_card)}")
            print("You Lose!")
            print("\n" * 5)
