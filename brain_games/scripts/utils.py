from random import randint


def random_number(max_value=10):
    return randint(1, max_value)


def wrong_answer(answer, c_answer, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{c_answer}'.")
    print(f"Let's try again, {name}!")
