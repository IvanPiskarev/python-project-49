from random import randint
from brain_games.cli import welcome_user


def even_game():
    name = welcome_user()
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        print("Answer 'yes' if number even otherwise answer 'no'.")
        print(f"Qusetion: {random_number}")
        answer = str(input("Your asnwer: ")).lower()
        condition_1 = random_number % 2 == 0 and answer == "yes"
        condition_2 = random_number % 2 != 0 and answer == "no"
        if condition_1 or condition_2:
            i += 1
            print("Correct!")
            if i == 3:
                print(f"Congratulations, {name}!")
                return True
        else:
            print("Wrong")
            restart = str(input("Do you want to try again? ")).lower()
            if restart == "yes":
                i = 0
            else:
                break
    return False
