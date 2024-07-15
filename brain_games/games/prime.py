import random


def prime_game():
    random_number = random.randint(1, 100)
    question = f"Question: {random_number}"
    if random_number == 1:
        correct_answer = "no"
    elif random_number == 2:
        correct_answer = "yes"
    i = 2
    count = 0
    while i < random_number:
        if random_number % i == 0:
            count += 1
            break
        else:
            i += 1
    if count == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
