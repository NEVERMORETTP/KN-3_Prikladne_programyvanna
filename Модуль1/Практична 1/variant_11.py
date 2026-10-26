def solve(a: str, b: str, op: str) -> str:
    allowed_ops = {"+", "-", "*", "/", "//", "%", "**"}
    if op not in allowed_ops:
        return "Помилка: невідомий оператор"

    try:
        if "." in a or "." in b:
            num1 = float(a)
            num2 = float(b)
        else:
            num1 = int(a)
            num2 = int(b)
    except ValueError:
        return "Помилка: некоректні дані"

    if op in {"/", "//", "%"} and num2 == 0:
        return "Помилка: ділення на нуль"

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    elif op == "//":
        result = num1 // num2
    elif op == "%":
        result = num1 % num2
    elif op == "**":
        result = num1 ** num2

    return str(result)


if __name__ == "__main__":
    val_a = input()
    val_b = input()
    operation = input()
    print(solve(val_a, val_b, operation))