import random


GAME_RULE = 'What number is missing in the progression?'


def random_progression():
    num = random.randint(1, 50)
    step = random.randint(1, 5)
    result = [num]
    for i in range(7):
        result.append(int(result[i]) + step)
    return result


def game():
    progression = random_progression()
    correct_answer = random.choice(progression)
    index = progression.index(correct_answer)
    progression[index] = ".."
    question = "Question: " + " ".join(map(str, progression))
    return question, correct_answer
