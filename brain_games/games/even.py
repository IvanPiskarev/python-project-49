import random


def even_game():
    random_number = random.randint(1, 100)
    question = f"Question: {random_number}"
    if random_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
