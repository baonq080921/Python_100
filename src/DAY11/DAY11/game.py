import random
import  black_jack_logo
import os
os.environ['TERM'] = 'xterm'
# list or card with Aces is 11 and J,Q,K is all 10
cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

is_over = True
is_going = True
while(is_over):
    count = 2
    your_card = []
    computer_card = []
    is_going = True
    # player, computer, max score
    current_score = 0
    max_score = 21
    final_score = 0
    start_game = input('Do you want to play a game of cards? (y/n): ').lower()

    if start_game == 'y' or start_game == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(black_jack_logo.blackjack_logo())
    if start_game =='n' or start_game == 'no':
        is_over = False
        break

    for i in range(count):
        your_card.append(cards[random.randint(0,len(cards)-1)])
        current_score += your_card[i]
    computer_card.append(cards[random.randint(0, len(cards) - 1)])
    print(f"Your card is:{your_card},current score:{current_score} " )
    while(current_score < max_score and is_going == True):
        print(f"Computer first card: {computer_card[0]}")
        get_next_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if get_next_card == 'y' or get_next_card == 'yes':
            your_card.append(cards[random.randint(0,len(cards)-1)])
            current_score += your_card[len(your_card) - 1]
            final_score = computer_card[len(computer_card)-1]
            print(f"Your card is:{your_card},current score:{current_score} ")
            if current_score > max_score:
                print(f"Computer's final hand: {computer_card}, final score:{final_score} ")
                print("You went over.You lose")
        elif get_next_card == 'n' or get_next_card=='pass':
            final_score = computer_card[len(computer_card) - 1]
            while final_score < 17:
                computer_card.append(cards[random.randint(0,len(cards)-1)])
                final_score += computer_card[len(computer_card) - 1]
            if final_score > max_score:
                print(f"Your card is:{your_card},current score:{current_score} ")
                print(f"Computer's final hand: {computer_card}, final score:{final_score} ")
                print("Opponent went over. You win")
            elif final_score < max_score:
                if final_score < current_score:
                    print(f"Your card is:{your_card},current score:{current_score} ")
                    print(f"Computer's final hand: {computer_card}, final score:{final_score} ")
                    print("You win")
                elif final_score > current_score:
                    print(f"Your card is:{your_card},current score:{current_score} ")
                    print(f"Computer's final hand: {computer_card}, final score:{final_score} ")

                    print("You lose")
                else:
                    print(f"Your card is:{your_card},current score:{current_score} ")
                    print(f"Computer's final hand: {computer_card}, final score:{final_score} ")

                    print("Draw")
            is_going = False









