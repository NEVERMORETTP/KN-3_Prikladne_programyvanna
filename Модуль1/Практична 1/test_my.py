import pytest
from variant_11 import solve


@pytest.mark.parametrize(
    "param1, param2, op, expected",
    [
        ("15", "0", "/", "Помилка: ділення на нуль"),
        ("10.5", "0.0", "%", "Помилка: ділення на нуль"),
        ("10", "2", "^", "Помилка: невідомий оператор"),
        ("abc", "5", "+", "Помилка: некоректні дані"),
        ("2", "5", "**", "32"),
        ("5.0", "2", "-", "3.0"),
    ],
)
def test_my_edge_cases(param1, param2, op, expected):
    assert solve(param1, param2, op) == expected