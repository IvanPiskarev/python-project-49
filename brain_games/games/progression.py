import random


def progression_game():
    random_number = random.randint(1, 50)
    random_step = random.randint(1, 5)
    progression = [random_number]
    for i in range(7):
        progression.append(int(progression[i]) + random_step)
    correct_answer = random.choice(progression)
    index = progression.index(correct_answer)
    progression[index] = ".."
    question = "Question: " + " ".join(map(str, progression))
    return question, correct_answer
