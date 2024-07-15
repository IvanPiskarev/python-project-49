from brain_games.cli import welcome_user


game_rules = {
    'even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'calc': 'What is the result of the expression?',
    'gcd': 'Find the greatest common divisor of given numbers.',
    'progression': 'What number is missing in the progression?',
    'prime': 'Answer "yes" if given number is prime. Otherwise answer "no".'
}


def play_game(game, rule):
    name = welcome_user()
    print(game_rules[rule])
    rounds = 0
    while rounds < 3:
        question, correct_answer = game()
        print(question)
        answer = str(input("Your asnwer: ")).lower()
        if answer == str(correct_answer):
            rounds += 1
            print("Correct!")
            if rounds == 3:
                print(f"Congratulations, {name}!")
                return True
        else:
            print(f'"{answer}" is wrong answer ;(.')
            print(f'Correct answer was "{correct_answer}".')
            break
    return False
