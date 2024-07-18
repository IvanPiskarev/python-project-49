import prompt
from brain_games.cli import welcome_user


game_rules = {
    'even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'calc': 'What is the result of the expression?',
    'gcd': 'Find the greatest common divisor of given numbers.',
    'progression': 'What number is missing in the progression?',
    'prime': 'Answer "yes" if given number is prime. Otherwise answer "no".'
}


def play_game(module):
    name = welcome_user()
    print(module.GAME_RULE)
    rounds = 0
    while rounds < 3:
        question, correct_answer = module.game()
        print(question)
        answer = prompt.string("Your asnwer: ")
        if answer == str(correct_answer):
            rounds += 1
            print("Correct!")
            if rounds == 3:
                print(f"Congratulations, {name}!")
                return True
        else:
            print(f'"{answer}" is wrong answer ;(.')
            print(f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            break
    return False
