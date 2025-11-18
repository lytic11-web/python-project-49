import random


def is_even(number: int) -> bool:
    return number % 2 == 0


def generate_round() -> tuple[str, str]:
    """Generate a round for the even game."""
    # For game purposes, using random is safe here
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
