import secrets


def generate_round() -> tuple[str, str]:
    # Параметры прогрессии
    start = secrets.randbelow(15) + 1  # начальное исло
    step = secrets.randbelow(10) + 1  # шаг
    length = secrets.randbelow(6) + 5  # длина

    # прогрессия
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))

    # случайная позиция скрытого элемента
    hidden_index = secrets.randbelow(length)
    carrect_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    guestion = " ".join(progression)

    return guestion, carrect_answer
