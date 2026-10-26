"""Завдання 1. Перевірка пароля (легке)."""


def solve(password: str) -> str:
    missing = []

    if len(password) < 8:
        missing.append("довжини")

    has_digit = any(ch.isdigit() for ch in password)
    if not has_digit:
        missing.append("цифри")

    has_upper = any(ch.isupper() for ch in password)
    if not has_upper:
        missing.append("великої літери")

    has_lower = any(ch.islower() for ch in password)
    if not has_lower:
        missing.append("малої літери")

    if not missing:
        return "Пароль прийнято"

    return f"Не вистачає: {', '.join(missing)}"


if __name__ == "__main__":
    pwd = input("Введіть пароль: ")
    print(solve(pwd))