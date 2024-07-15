import random
from brain_games.cli import welcome_user
from brain_games.scripts.utils import wrong_answer


def calc():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    arithmetic_operations = ["+", "-", "*"]
    random_operator = random.choice(arithmetic_operations)
    question = f"{first_number} {random_operator} {second_number}"
    if random_operator == "+":
        correct_answer = first_number + second_number
    elif random_operator == "-":
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return question, correct_answer


def calc_game():
    name = welcome_user()
    print("What is the result of the expression?")
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
