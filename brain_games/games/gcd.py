import math
import secrets


def generate_round() -> tuple[str, str]:
    num1 = secrets.randbelow(50) + 1  # 1-50
    num2 = secrets.randbelow(50) + 1  # 1-50

    guestion = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))

    return guestion, correct_answer
