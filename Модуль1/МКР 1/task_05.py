"""Завдання 5. Частоти символів (середнє)."""


def solve(text: str) -> str:
    cleaned_chars = [ch.lower() for ch in text if not ch.isspace()]
    if not cleaned_chars:
        return "Порожній текст"

    freq = {}
    for ch in cleaned_chars:
        freq[ch] = freq.get(ch, 0) + 1

    distinct_count = len(freq)

    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    top_5 = sorted_items[:5]

    lines = [f"{char}: {count}" for char, count in top_5]
    lines.append(f"Різних символів: {distinct_count}")
    return "\n".join(lines)


if __name__ == "__main__":
    txt = input("Введіть текст: ")
    print(solve(txt))