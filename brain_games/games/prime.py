import random


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    x = 2
    while x < num:
        if num % x == 0:
            return False
        else:
            x += 1
    return True


def game():
    num = random.randint(1, 100)
    question = f"Question: {num}"
    if is_prime(num) is True:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
