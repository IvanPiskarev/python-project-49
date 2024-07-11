from brain_games.cli import welcome_user
from brain_games.scripts.utils import random_number, wrong_answer


def even_game():
    name = welcome_user()
    rounds = 0
    while rounds < 3:
        number = random_number(100)
        print("Answer 'yes' if number even otherwise answer 'no'.")
        print(f"Qusetion: {number}")
        answer = str(input("Your asnwer: ")).lower()
        if number % 2 == 0:
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
