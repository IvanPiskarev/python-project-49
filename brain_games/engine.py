import prompt
from brain_games.cli import welcome_user


def play_game(module):
    """Asks the questions and checks the correctness of the answers"""
    name = welcome_user()
    print(module.GAME_RULE)
    rounds = 3
    for i in range(rounds):
        question, correct_answer = module.game()
        print(question)
        answer = prompt.string("Your asnwer: ")
        if answer == str(correct_answer):
            print("Correct!")
        else:
            print(f'"{answer}" is wrong answer ;(.')
            print(f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return False
    print(f"Congratulations, {name}!")
    return True
