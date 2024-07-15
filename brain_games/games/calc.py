import random


def calc_game():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    arithmetic_operations = ["+", "-", "*"]
    random_operator = random.choice(arithmetic_operations)
    question = f"Question: {first_number} {random_operator} {second_number}"
    if random_operator == "+":
        correct_answer = first_number + second_number
    elif random_operator == "-":
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return question, correct_answer
