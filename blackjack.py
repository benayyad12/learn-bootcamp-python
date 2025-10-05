import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)

def calculate_score(cards_):
    if len(cards_)==2 and sum(cards_)==21:
        return 0
    if len(cards_)==2 and 11 in cards_ and sum(cards_) > 21:
        cards_.remove(11)
        cards_.append(1)
    return sum(cards_)
    
def compare(u_score, c_score):
    if u_score==c_score:
        print("It's a draw")
    elif c_score==0:
        print("You lose, computer has a BJ ")
    elif u_score==0:
        print("You win")
    elif u_score > 21:
        print("You lose")
    elif u_score > c_score:
        print("you win")
    else:
        print("You lose")

def game():
    print(r"""
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
            |  \/ K|                            _/ |                
            `------'                           |__/           
        """
        )
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, Your current score is: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score==0 or computer_score==0 or user_score > 21:
            print("The game end!")
            is_game_over = True
        else:
            draw_card = input("Do you want to draw another card? 'y' or 'n': ")
            if draw_card=='y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                print("The game end")
                is_game_over = True

    while computer_score!=0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    compare(user_score,computer_score)



restart_game = input("Start a new game: 'y' or 'n' ")
while restart_game == 'y':
    print("\n"*20)
    game()

