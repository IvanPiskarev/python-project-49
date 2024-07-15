import random
import math
from brain_games.cli import welcome_user
from brain_games.scripts.utils import wrong_answer


def gcd(first_number, second_number):
    return math.gcd(first_number, second_number)


def gcd_game():
    name = welcome_user()
    rounds = 0
    while rounds < 3:
        first_number = random.randint(2, 100)
        second_number = random.randint(2, 100)
        correct_answer = gcd(first_number, second_number)
        print("Find the greatest common divisor of given numbers.")
        print(f"Question: {first_number} {second_number}")
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
