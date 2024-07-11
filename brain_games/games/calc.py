from random import choice
from brain_games.cli import welcome_user
from brain_games.scripts.utils import random_number, wrong_answer


def calc():
    number_1 = random_number()
    number_2 = random_number()
    arithmetic_operations = ["+", "-", "*"]
    random_operator = choice(arithmetic_operations)
    if int(number_1) > int(number_2):
        question = f"{number_1} {random_operator} {number_2}"
        if random_operator == "+":
            correct_answer = number_1 + number_2
        elif random_operator == "-":
            correct_answer = number_1 - number_2
        else:
            correct_answer = number_1 * number_2
    else:
        question = f"{number_2} {random_operator} {number_1}"
        if random_operator == "+":
            correct_answer = number_2 + number_1
        elif random_operator == "-":
            correct_answer = number_2 - number_1
        else:
            correct_answer = number_2 * number_1
    return question, correct_answer


def calc_game():
    name = welcome_user()
    rounds = 0
    while rounds < 3:
        question, correct_answer = calc()
        print(question)
        answer = int(input("Your asnwer: "))
        if answer == int(correct_answer):
            rounds += 1
            print("Correct!")
            if rounds == 3:
                print("Congratulations!")
                return True
        else:
            wrong_answer(answer, correct_answer, name)
            break
    return False
