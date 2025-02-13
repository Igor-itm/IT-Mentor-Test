# module: itm_test.py

import re


def calculate(operator: str, a: int, b: int) -> int:
    actions = {
        '+': int.__add__,
        '-': int.__sub__,
        '/': lambda x,y: int.__divmod__(x, y)[0],
        '*': int.__mul__,
    }
    return actions[operator](a, b)


def get_number(num_str: str, lo=1, hi=10) -> int:
    try:
        num = int(num_str)
    except ValueError:
        raise Exception(f"Ошибка при вводе целого числа. Введено: '{num_str}'")

    if not (lo <= num <= hi):
       raise Exception(f"Число вне диапазона от {lo} до {hi} включительно. Введено: '{num_str}'")
    return num


def split_expression(expression: str):
    # Регулярное выражение для разделения строки на 3 части: a, operator, b
    pattern = r'^( *[-+]*[^-+/*]*)([-+/*]?)(.*)$'
    match = re.match(pattern, expression)

    if match:
        a = match.group(1) if match.group(1) else ''
        operator = match.group(2) if match.group(2) else ''
        b = match.group(3) if match.group(3) else ''
        return a, operator, b
    else:
        return None, None, None


def main(expression: str) -> str:
    a, operator, b = split_expression(expression)
    if operator:
        if not b.strip().isdigit():
            raise Exception(f"Ошибка при вводе целого числа. Введено: '{operator}{b}'")

        a, b = map(get_number, [a, b])
        return str(calculate(operator, a, b))
    else:
        raise Exception("Строка не является математической операцией.")


if __name__ == '__main__':
    input_str: str = input("Введите выражение: ")
    result: str = main(input_str)

    print(f"Результат: {result}")
