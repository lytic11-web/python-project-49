import random


def is_even(namber: int) -> bool:
    return namber % 2 == 0


def generate_round() -> tuple:
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
