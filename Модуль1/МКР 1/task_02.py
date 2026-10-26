"""Завдання 2. Таблиця множення (легке)."""


def solve(n: str) -> str:
    cleaned = n.strip()
    if not cleaned.isdigit():
        return "Помилка: n має бути цілим від 1 до 12"

    val = int(cleaned)
    if val < 1 or val > 12:
        return "Помилка: n має бути цілим від 1 до 12"

    lines = []
    total = 0
    for k in range(1, 11):
        prod = val * k
        total += prod
        lines.append(f"{val} x {k} = {prod}")

    lines.append(f"Сума: {total}")
    return "\n".join(lines)


if __name__ == "__main__":
    val = input("Введіть число від 1 до 12: ")
    print(solve(val))