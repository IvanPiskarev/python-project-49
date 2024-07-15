import random
from brain_games.cli import welcome_user
from brain_games.scripts.utils import wrong_answer


def even_game():
    name = welcome_user()
    rounds = 0
    while rounds < 3:
        random_number = random.randint(1, 100)
        print("Answer 'yes' if the number is even, otherwise answer 'no'.")
        print(f"Question: {random_number}")
        answer = str(input("Your asnwer: ")).lower()
        if random_number % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        if answer == correct_answer:
            rounds += 1
            print("Correct!")
            if rounds == 3:
                print(f"Congratulations, {name}!")
                return True
        else:
            wrong_answer(answer, correct_answer, name)
            break
    return False
