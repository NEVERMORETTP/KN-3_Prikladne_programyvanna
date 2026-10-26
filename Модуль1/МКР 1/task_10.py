"""Завдання 10. Ледачі вікна й серії (складне)."""

from collections import deque


def windows(items, k: int):
    if k <= 0:
        raise ValueError("k має бути додатним")

    it = iter(items)
    window = deque()

    for _ in range(k):
        try:
            window.append(next(it))
        except StopIteration:
            return

    yield tuple(window)

    for item in it:
        window.popleft()
        window.append(item)
        yield tuple(window)


def run_lengths(items):
    it = iter(items)
    try:
        current_item = next(it)
    except StopIteration:
        return

    count = 1
    for item in it:
        if item == current_item:
            count += 1
        else:
            yield (current_item, count)
            current_item = item
            count = 1
    yield (current_item, count)


def best_window(values: list[int], k: int) -> tuple | None:
    if k <= 0:
        raise ValueError("k має бути додатним")

    if len(values) < k:
        return None

    max_sum = None
    best_idx = 0

    for idx, win in enumerate(windows(values, k)):
        current_sum = sum(win)
        if max_sum is None or current_sum > max_sum:
            max_sum = current_sum
            best_idx = idx

    return (best_idx, max_sum)


if __name__ == "__main__":
    raw_nums = input("Введіть числа списку через пробіл (наприклад: 1 5 2 8 1): ")
    numbers = [int(x) for x in raw_nums.split() if x.strip()]
    k_size = int(input("Введіть розмір вікна k (наприклад: 2): "))

    print("Вікна:", list(windows(numbers, k_size)))
    print("Серії повторів:", list(run_lengths(numbers)))
    print("Найкраще вікно (індекс початку, сума):", best_window(numbers, k_size))