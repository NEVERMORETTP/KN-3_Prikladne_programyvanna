def solve(seq_str: str) -> str:
    raw_tokens = seq_str.split()
    if len(raw_tokens) == 0:
        return "Помилка: некоректні числа"

    numbers = []
    for token in raw_tokens:
        s = token
        if s.startswith("-"):
            s = s[1:]
        if len(s) == 0 or not s.isdigit():
            return "Помилка: некоректні числа"
        numbers.append(int(token))

    if len(numbers) < 3:
        return "Кількість піків: 0"

    peak_positions = []
    peak_values = []

    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            peak_positions.append(str(i + 1))
            peak_values.append(numbers[i])

    k = len(peak_positions)
    if k == 0:
        return "Кількість піків: 0"

    highest_peak = peak_values[0]
    for val in peak_values:
        if val > highest_peak:
            highest_peak = val

    positions_str = ", ".join(peak_positions)
    return (
        f"Кількість піків: {k}\n"
        f"Позиції: {positions_str}\n"
        f"Найвищий пік: {highest_peak}"
    )


if __name__ == "__main__":
    data = input()
    print(solve(data))