import math
import secrets


def is_prime(number: int) -> bool:
    # Check if a number is prime 
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # Check only odd divisors up to sqrt(number)
    limit = math.isqrt(number)
    for divisor in range(3, limit + 1, 2):
        if number % divisor == 0:
            return False
    
    return True


def generate_round() -> tuple[str, str]:
    number = secrets.randbelow(100) + 1  # 1-100
    
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    
    return question, correct_answer
