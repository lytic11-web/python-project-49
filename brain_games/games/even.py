import secrets


def is_even(number: int) -> bool:
    return number % 2 == 0


def generate_round() -> tuple[str, str]:
    """Generate a round for the even game."""
    # Using secrets for cryptographically secure randomness
    number = secrets.randbelow(100) + 1  # 1-100
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
