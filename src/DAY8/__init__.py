import string


def life_in_weeks(age)-> str:

    years = 90 - age
    weeks_left = years * 52
    return f'You have {weeks_left} weeks left'

age_input = int(input('Input your age: '))
test = life_in_weeks(age=age_input)
print(test)