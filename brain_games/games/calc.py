import random


GAME_RULE = 'What is the result of the expression?'


def calc(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    else:
        result = num1 * num2
    return result


def game():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    arithmetic_operators = ["+", "-", "*"]
    operator = random.choice(arithmetic_operators)
    question = f"Question: {num1} {operator} {num2}"
    correct_answer = calc(num1, num2, operator)
    return question, correct_answer
