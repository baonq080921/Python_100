import random

print("HANG MAN:")
print("\n")

keyword = 'apple'
# random_int =random.randint(1,5)
random_int = len(keyword)
word_guess =""
for i  in range (1,random_int+1):
    word_guess+="_"
print("Word to guess:"+word_guess)

user_input = input("Press any key to continue")
player_won = False

count =0
correct_letter =[]
while(player_won == False):
    display = ""
    user_input = input("Guess a letter")
    for letter in keyword:
        if letter == user_input:
            display += letter
            correct_letter.append(user_input)
        elif letter in correct_letter:
            display += letter

        elif letter != user_input:
            display += "_"
            count = 4

    print(display)

    if "_" not in display:
        player_won = True
        print("Congratulations! You won")







