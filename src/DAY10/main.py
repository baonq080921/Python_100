import caculator_art
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def test():
    caculator_art.caculator_art()
    is_continue = True
    numbers = 0
    first_number = float(input("What is your first number? "))
    user_caculator = True
    while is_continue:
        operations = ['+', '-', '*', ':']
        for operation in operations:
            print(operation)
        operation = input("Pick an operation:")
        second_number = float(input("What is your next number?"))
        if operation == '+':
            numbers = add(first_number,second_number)
            print(f"{first_number}{operation}{second_number}={numbers}")
            first_number = numbers
        elif operation == '-':
            numbers=subtract(first_number,second_number)
            print(f"{first_number}{operation}{second_number}={numbers}")
            first_number = numbers
        elif operation=='*':
            numbers=multiply(first_number, second_number)
            print(f"{first_number}{operation}{second_number}={numbers}")
            first_number = numbers

        elif operation==':' or operation =='/':
            numbers=divide(first_number,second_number)
            print(f"{first_number}{operation}{second_number}={numbers}")
            first_number = numbers

        keep_caculating = input(f"Type 'y' to continue calculating with {numbers}, or type 'n' to start a new calculation, or 'q' to quit: :")
        if keep_caculating=='y':
            is_continue = True
        elif keep_caculating == 'n':
            is_continue = False
            test()
        elif keep_caculating=='q':
            print("Thanks for using this.Good Bye!!!")
            is_continue =False

test()