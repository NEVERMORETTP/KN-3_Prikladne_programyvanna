def parse_items(text: str) -> list:
    items = []
    tokens = text.split()
    for token in tokens:
        if token.startswith("+380") and len(token) == 13 and token[1:].isdigit():
            items.append(token[4:6])
        elif token.startswith("0") and len(token) == 10 and token.isdigit():
            items.append(token[1:3])
    return items


def build_index(items: list) -> dict:
    index = {}
    for item in items:
        index[item] = index.get(item, 0) + 1
    return index


def rank(index: dict, n: int) -> list:
    if n <= 0:
        return []
    sorted_pairs = sorted(index.items(), key=lambda pair: (-pair[1], pair[0]))
    return sorted_pairs[:n]


def unique_sorted(items: list) -> list:
    return sorted(list(set(items)))


def solve(text: str, n: str) -> str:
    n_cleaned = n.strip()
    if not n_cleaned or not n_cleaned.isdigit():
        return "Помилка: n має бути цілим невід'ємним числом"

    n_val = int(n_cleaned)
    items = parse_items(text)
    if not items:
        return "Помилка: немає даних"

    unique_items = unique_sorted(items)
    index = build_index(items)
    top_ranked = rank(index, n_val)

    lines = [
        f"Номерів: {len(items)}",
        f"Унікальних кодів: {len(unique_items)}",
        f"Найпоширеніші коди (топ-{n_val}):",
    ]

    for i, (code, count) in enumerate(top_ranked, start=1):
        lines.append(f"{i}. {code}: {count}")

    return "\n".join(lines)


if __name__ == "__main__":
    input_text = input()
    input_n = input()
    print(solve(input_text, input_n))