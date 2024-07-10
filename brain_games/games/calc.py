from brain_games.cli import welcome_user
from brain_games.scripts.utils import calc, wrong_answer


def calc_game():
    name = welcome_user()
    rounds = 0
    while rounds < 3:
        question, correct_answer = calc()
        print(question)
        answer = int(input("Your asnwer: "))
        if answer == int(correct_answer):
            rounds += 1
            print("Correct!")
            if rounds == 3:
                print("Congratulations!")
                return True
        else:
            wrong_answer(answer, correct_answer, name)
            break
    return False
