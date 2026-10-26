"""Завдання 7. Лічильник із замиканням (середнє)."""

from typing import Callable


def make_counter(step: int) -> Callable[[], int]:
    current = 0

    def counter() -> int:
        nonlocal current
        current += step
        return current

    return counter


def apply_n(f: Callable[[], int], n: int) -> list[int]:
    if n <= 0:
        return []
    return [f() for _ in range(n)]


if __name__ == "__main__":
    step_val = int(input("Введіть крок лічильника (наприклад, 3): "))
    count_val = int(input("Введіть кількість викликів (наприклад, 4): "))
    counter_fn = make_counter(step_val)
    print("Результат роботи лічильника:", apply_n(counter_fn, count_val))