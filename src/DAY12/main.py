from logo import logo_print
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS  = 5


def set_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level =="easy":
        return EASY_LEVEL_TURNS
        
    elif level =='n':
        return HARD_LEVEL_TURNS
def check_answer(guess,random_number):
    
    if guess == random_number:
        return 0
    elif guess < random_number:
       
        return 1
    elif guess > random_number:
        return 2        
    
    

def main():
    random_number = random.randint(1,100)
    is_over = False
    logo = logo_print()
    print (logo)
    print("Welcome to the Number Guessing Game!")
    print("\nI'm thinking of a number between 1 and 100.")
    lives = set_level()
   
    while not is_over:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        x = check_answer(guess,random_number)
        if x ==0:
            print("You Won!")
            is_over = True
        elif x==1:
            print('Too Low')
            lives -=1
        elif x == 2:
            print('Too HIGH')
            lives -=1
            
        
        if lives ==0:
            is_over = True
        
            
        
                   
main()
    