import  random
import black_jack_logo
import  os
os.environ['TERM'] = 'xterm'
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card(cards):
    return  random.choice(cards)


def caculate_score(card):
    return sum(card)

def main():
    is_over = False

    while (is_over ==False):
        user_score = 0
        computer_score = 0
        is_going = True
        max_score = 21
        user_card = []
        computer_card = []

        start_game = input('Do you want to play a game of cards? (y/n): ').lower()
        for i in range(2):
            user_card.append(deal_card(cards))
        computer_card.append(deal_card(cards))

        user_score = caculate_score(user_card)
        computer_score = caculate_score(computer_card)

        if user_score == 21:
            print(f"Your cards: {user_card}, Blackjack! You win!")
            continue

        if start_game == 'y' or start_game == 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(black_jack_logo.blackjack_logo())
        if start_game == 'n' or start_game == 'no':
            is_over = True
        while is_going:
            print(f"Your cards:{user_card},current score: {user_score}")
            print(f"Computer's first card: {computer_card}")
            get_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if get_card == 'y':
                user_card.append(deal_card(cards))
                user_score = caculate_score(user_card)
                if(user_score > max_score):
                    print(f"Your cards:{user_card},current score: {user_score}")
                    print(f"Computer's final hand: {computer_card}, final score:{computer_score} ")
                    print("You went over.You lose")
                    is_going =False
            elif get_card == 'n':
                is_going =False

                while(computer_score < 17):
                    computer_card.append(deal_card(cards))
                    computer_score = caculate_score(computer_card)

                if(computer_score > max_score):
                    print(f"Your card is:{user_card},current score:{user_score} ")
                    print(f"Computer's final hand: {computer_card}, final score:{computer_score} ")
                    print("Opponent went over. You win")
                elif computer_score < max_score:
                    if computer_score < user_score:
                        print(f"Your card is:{user_card},current score:{user_score} ")
                        print(f"Computer's final hand: {computer_card}, final score:{computer_score} ")
                        print("You win")
                    elif computer_score > user_score:
                        print(f"Your card is:{user_card},current score:{user_score} ")
                        print(f"Computer's final hand: {computer_card}, final score:{computer_score} ")

                        print("You lose")
                    else:
                        print(f"Your card is:{user_card},current score:{user_score} ")
                        print(f"Computer's final hand: {computer_card}, final score:{computer_score} ")

                        print("Draw")





if __name__ == '__main__':
    main()


