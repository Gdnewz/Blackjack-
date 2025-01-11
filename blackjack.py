import random
import art1

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if c_score == u_score:
        return "DRAW :/"


    elif c_score == 0:
        return "You Lose :(, opponent had BlackJack"


    elif u_score == 0:
        return "You win with a BlackJack :)"


    elif u_score > 21:
        return "You lose, you went over :("

    elif c_score > 21:
        return "Opponent went over. You win :)"


    elif u_score > c_score:
        return "Your score was higher. You win :)"

    else:
        return "Opponent got higher score. You lose :("


def to_restart():
    print(art1.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for cards in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True


        else:
            to_continue = input("Do you want to draw another card? Type 'yes' or 'no': ")
            if to_continue == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
       computer_cards.append(deal_card())
       computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 25)
    to_restart()



