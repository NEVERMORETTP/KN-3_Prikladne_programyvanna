import pytest
from variant_11 import parse_items, build_index, rank, unique_sorted, solve


def test_parse_items():
    text = "+380671234567 0671234567 12345 +380501112233 099123456"
    assert parse_items(text) == ["67", "67", "50"]


def test_build_index():
    items = ["67", "67", "50", "99", "67"]
    assert build_index(items) == {"67": 3, "50": 1, "99": 1}


def test_rank():
    index = {"50": 2, "67": 2, "99": 1}
    assert rank(index, 2) == [("50", 2), ("67", 2)]
    assert rank(index, 0) == []


def test_unique_sorted():
    items = ["67", "50", "67", "99", "50"]
    assert unique_sorted(items) == ["50", "67", "99"]


@pytest.mark.parametrize(
    "text, n, expected",
    [
        (
            "+380671234567 0671234567 0501112233",
            "2",
            "Номерів: 3\nУнікальних кодів: 2\nНайпоширеніші коди (топ-2):\n1. 67: 2\n2. 50: 1",
        ),
        ("bad_token 123", "2", "Помилка: немає даних"),
        ("+380671234567", "abc", "Помилка: n має бути цілим невід'ємним числом"),
    ],
)
def test_solve(text, n, expected):
    assert solve(text, n) == expected