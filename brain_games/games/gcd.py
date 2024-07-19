import random
import math


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def game():
    """Generates 2 random numbers and determines their gcd"""
    num1 = random.randint(2, 100)
    num2 = random.randint(2, 100)
    question = f"Question: {num1} {num2}"
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer
