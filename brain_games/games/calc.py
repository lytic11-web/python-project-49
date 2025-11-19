import secrets
import operator


def calculate(num1: int, num2: int, operation: str) -> int:
    """Calculate the result of two numbers with given operation."""
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    return operations[operation](num1, num2)


def generate_round() -> tuple[str, str]:
    """Generate a round for the calculator game."""
    num1 = secrets.randbelow(50) + 1  # 1-50
    num2 = secrets.randbelow(50) + 1  # 1-50
    operation = secrets.choice(['+', '-', '*'])

    question = f"{num1} {operation} {num2}"
    correct_answer = str(calculate(num1, num2, operation))

    return question, correct_answer
