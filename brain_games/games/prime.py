import random
from brain_games.cli import welcome_user
from brain_games.scripts.utils import wrong_answer


def prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    i = 2
    while i < number:
        if number % i == 0:
            return False
        else:
            i += 1
    return True


def prime_game():
    name = welcome_user()
    rounds = 0
    while rounds < 3:
        random_number = random.randint(1, 100)
        print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
        print(f"Qusetion: {random_number}")
        answer = str(input("Your asnwer: ")).lower()
        if prime(random_number) is True:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        if answer == correct_answer:
            rounds += 1
            print("Correct!")
            if rounds == 3:
                print("Congratulations")
                return True
        else:
            wrong_answer(answer, correct_answer, name)
            break
    return False
