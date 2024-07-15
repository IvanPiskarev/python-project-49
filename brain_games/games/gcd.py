import random
import math


def gcd_game():
    first_number = random.randint(2, 100)
    second_number = random.randint(2, 100)
    question = f"Question: {first_number} {second_number}"
    correct_answer = math.gcd(first_number, second_number)
    return question, correct_answer
