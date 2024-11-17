import random
import _hang_man_art as  art
print(art.logo)
def main():
    lives = 6
    correct_letter = []
    i =0
    game_end = False
    keyword = ['apple', 'banana', 'cherry','grape','orange','pear','watermelon']
    # random_int =random.randint(1,5)
    random_choice = random.choice(keyword)
    print(random_choice)
    n = len(random_choice)
    print(n)
    word_guess =""
    for i  in range (1,n+1):
        word_guess+="_"
    print("Word to guess:"+word_guess)
    print('\n')
    user_input = input("Press any key to continue")
    player_won = False
    while(not game_end):
        display = ""
        user_input = input("Guess a letter:")

        for letter in random_choice:
            if letter == user_input:
                display += letter
                correct_letter.append(user_input)
            elif letter in correct_letter:
                display += letter

            elif letter != user_input:
                display += "_"
        print(display)

        if user_input in correct_letter:
            print(f"You've already guessed {letter}")
            print(art.stages[lives])
        elif user_input not in correct_letter:
            lives -= 1
            print(f'You guess {user_input} wrong letter, Please try again')
            print(art.stages[lives])
            if (lives == 0):
                game_end = True
                print('You lose')

        if "_" not in display:
            game_end=True
            print("Congratulations! You won")
if __name__ == "__main__":
    main()






