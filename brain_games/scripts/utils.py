from random import randint, choice


def random_number():
    return randint(1, 10)


def calc():
    number_1 = random_number()
    number_2 = random_number()
    arithmetic_operations = ["+", "-", "*"]
    random_operator = choice(arithmetic_operations)
    if int(number_1) > int(number_2):
        question = f"{number_1} {random_operator} {number_2}"
        if random_operator == "+":
            correct_answer = number_1 + number_2
        elif random_operator == "-":
            correct_answer = number_1 - number_2
        else:
            correct_answer = number_1 * number_2
    else:
        question = f"{number_2} {random_operator} {number_1}"
        if random_operator == "+":
            correct_answer = number_2 + number_1
        elif random_operator == "-":
            correct_answer = number_2 - number_1
        else:
            correct_answer = number_2 * number_1
    return question, correct_answer


def progression():
    number = random_number
    random_step = randint(1, 5)
    result = [number]
    for i in range(7):
        result.append(int(result[i]) + random_step)
    return result


def prime_number(number):
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


def wrong_answer(answer, c_answer, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{c_answer}'.")
    print(f"Let's try again, {name}!")
