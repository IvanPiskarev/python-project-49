import random
from brain_games.cli import welcome_user
from brain_games.scripts.utils import wrong_answer


def random_progression():
    random_number = random.randint(1, 50)
    random_step = random.randint(1, 5)
    result = [random_number]
    for i in range(7):
        result.append(int(result[i]) + random_step)
    return result


def progression_game():
    name = welcome_user()
    rounds = 0
    while rounds < 3:
        progression = random_progression()
        correct_answer = random.choice(progression)
        index = progression.index(correct_answer)
        progression[index] = ".."
        print("Question: " + " ".join(map(str, progression)))
        answer = int(input("Your asnwer: "))
        if answer == int(correct_answer):
            rounds += 1
            print("Correct!")
            if rounds == 3:
                print(f"Congratulations, {name}!")
                return True
        else:
            wrong_answer(answer, correct_answer, name)
            break
    return False
