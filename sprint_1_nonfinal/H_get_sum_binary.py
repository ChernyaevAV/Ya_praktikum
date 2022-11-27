from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:

    max_number = max(
        len(first_number),
        len(second_number)
    )
    num1 = first_number.zfill(max_number)
    num2 = second_number.zfill(max_number)

    stack = 0
    result = []
    for elem in zip(num1[::-1], num2[::-1]):
        value = int(elem[0]) + int(elem[1]) + stack
        stack = value // 2
        result.append(value % 2)

    if stack == 1:
        result.append(1)

    result = ''.join(map(str, result))[::-1]
    return result


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))