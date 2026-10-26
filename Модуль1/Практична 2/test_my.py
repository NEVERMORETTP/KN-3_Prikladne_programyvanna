import pytest
from variant_11 import solve


@pytest.mark.parametrize(
    "data, expected",
    [
        ("1 3 2 4 1", "Кількість піків: 2\nПозиції: 2, 4\nНайвищий пік: 4"),
        ("5 4 3 2 1", "Кількість піків: 0"),
        ("10 20", "Кількість піків: 0"),
        ("-5 -2 -4 -1 -3", "Кількість піків: 2\nПозиції: 2, 4\nНайвищий пік: -1"),
        ("1 2 abc", "Помилка: некоректні числа"),
        ("", "Помилка: некоректні числа"),
    ],
)
def test_my_edge_cases(data, expected):
    assert solve(data) == expected